from django.contrib import admin
from .models import Post, Comment , User


class PostAdmin(admin.ModelAdmin):
    listDisplay = ['title', 'text']


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    listDisplay = ['post', 'text']


admin.site.register(Comment, CommentAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display =['username' , 'email']


admin.site.register(User , UserAdmin)
