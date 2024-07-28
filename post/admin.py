from django.contrib import admin
from .models import Post, Comment, CustomUser


class PostAdmin(admin.ModelAdmin):
    listDisplay = ['title', 'text']


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    listDisplay = ['pk', 'post', 'text']


admin.site.register(Comment, CommentAdmin)


class CustomUserAdmin(admin.ModelAdmin):
    listDisplay = ['username', 'email', 'password']


admin.site.register(CustomUser, CustomUserAdmin)
