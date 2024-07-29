from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:postsId>/', views.postDetail , name = 'post_detail'),
    path('' , views.homePage , name = 'home'),
    path('posts/', views.postList , name = 'post_list'),
    path('posts/', views.postList, name='post_list'),
    path('postlist/', views.createPost, name='create_post'),
    path('commentlist/<int:postId>/comments/', views.createComment, name='create_comment'),
    path('login_register/', views.login_register, name='login_register'),
    path('test/' , views.test),
    path('logout/', views.logout_view, name='logout'),


]
