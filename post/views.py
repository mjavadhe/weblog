from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post , Comment
from .forms import PostForm , CommentForm


def homePage(request):
    return render(request , 'homepage.html')


def postList(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request , 'postlist.html' , context)


def postDetail(request ,postsId):
    post = Post.objects.get(pk = postsId)
    posts = Post.objects.get(pk = postsId) , Post.objects.all()
    comments = Comment.objects.filter(post = post)
    context = {'posts':posts , 'comments' : comments}
    return render(request , 'postdetail.html' , context)


def createPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('create_post'))
    else:
        form = PostForm()
    return render(request, 'createpost.html', {'form': form})


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


def test(request):
    return render (request , 'test.html')