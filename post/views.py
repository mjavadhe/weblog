from django.shortcuts import render ,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import P , C , CustomUser
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
    posts = P.objects.all()
    context = {'posts' : posts}
    return render(request , 'postlist.html' , context)

@login_required(login_url='/login_register/')
def postDetail(request ,postsId):
    post = P.objects.get(pk = postsId)
    posts = P.objects.get(pk = postsId) , P.objects.all()
    comments = C.objects.filter(post = post)
    context = {'posts':posts , 'comments' : comments}
    return render(request , 'postdetail.html' , context)


@login_required(login_url='/login_register/')
def createComment(request, postId):
    post = P.objects.get(pk=postId)
    if request.method == 'POST':
        text = request.POST.get('text')

        if text:
            C.objects.create(author=request.user  , post=post, text=text)
            return HttpResponseRedirect(reverse('post_detail', args=[postId]))
    return render(request, 'createcomment.html', {'post': post})


@login_required(login_url='/login_register/')
def createPost(request):
    user = CustomUser.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'createpost.html', {'form': form , 'user' : user})

def login_register(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = CustomUser.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('home')
        elif 'login' in request.POST:
            login_identifier = request.POST.get('login_identifier')
            password = request.POST.get('password')
            user = CustomUser.objects.filter(email=login_identifier).first() or CustomUser.objects.filter(username=login_identifier).first()
            if user:
                user = authenticate(request, username=user.username, password=password)
                if user is not None and user.is_active:
                    login(request, user)
                    return redirect('home')

    return render(request, 'form.html')


@login_required(login_url='/login_register/')
def profile(request):
    return render(request , 'profile.html')


@login_required(login_url='/login_register/')
def commentList(request ,id):
    post = P.objects.get(pk = id)
    posts = P.objects.get(pk = id) , P.objects.all()
    comments = C.objects.filter(post = post)
    context = {'posts':posts , 'comments' : comments}
    return render(request , 'commentlist.html' , context)


@login_required(login_url='/login_register/')
def userProfile(request, postId):
    user = CustomUser.objects.get(pk=postId)
    if request.method == 'POST':
        text = request.POST.get('text')
        post = P.oblects.all()
        context = {'user' : user ,'post' : post}

        if text:
            C.objects.create(author=request.user  , user=user, text=text)
            return HttpResponseRedirect(reverse('post_detail', args=[postId]))
    return render(request, 'userprofile.html', {'user': user})

