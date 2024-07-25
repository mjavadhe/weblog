from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    listDisplay = ['title', 'text']


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    listDisplay = ['post', 'text']


admin.site.register(Comment, CommentAdmin)
