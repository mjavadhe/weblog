from django.shortcuts import render ,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post , Comment , CustomUser
from .forms import PostForm , CommentForm
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required(login_url='/login_register/')
def logout_view(request):
    logout(request)
    return redirect('login_register')


@login_required(login_url='/login_register/')
def homePage(request):
    return render(request , 'homepage.html')

@login_required(login_url='/login_register/')
def postList(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request , 'postlist.html' , context)

@login_required(login_url='/login_register/')
def postDetail(request ,postsId):
    post = Post.objects.get(pk = postsId)
    posts = Post.objects.get(pk = postsId) , Post.objects.all()
    comments = Comment.objects.filter(post = post)
    context = {'posts':posts , 'comments' : comments}
    return render(request , 'postdetail.html' , context)


@login_required(login_url='/login_register/')
def createPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('post_list'))
    else:
        form = PostForm()
    return render(request, 'createpost.html', {'form': form})


@login_required(login_url='/login_register/')
def createComment(request, postId):
    post = Post.objects.get(pk=postId)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post_detail', args=[postId]))
    else:
        form = CommentForm()
    return render(request, 'createcomment.html', {'form': form, 'post': post})


def login_register(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            register_form = CustomUserCreationForm(request.POST)
            login_form = CustomAuthenticationForm()
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect('home')
        elif 'login' in request.POST:
            login_form = CustomAuthenticationForm(data=request.POST)
            register_form = CustomUserCreationForm()
            if login_form.is_valid():
                user = authenticate(username=login_form.cleaned_data['username'],
                                    password=login_form.cleaned_data['password'])
                if user is not None and user.is_active:
                    login(request, user)
                    return redirect('home')


    else:
        login_form = CustomAuthenticationForm()
        register_form = CustomUserCreationForm()

    return render(request, 'login_register.html', {'login_form': login_form, 'register_form': register_form})





def test(request):
    return render (request , 'test.html')