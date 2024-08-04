from django.contrib import admin
from .models import P, C, CustomUser


class PAdmin(admin.ModelAdmin):
    listDisplay = ['author','title', 'text']


admin.site.register(P, PAdmin)


class CAdmin(admin.ModelAdmin):
    listDisplay = ['author', 'post', 'text']


admin.site.register(C, CAdmin)


class CustomUserAdmin(admin.ModelAdmin):
    listDisplay = ['username', 'email', 'password']


admin.site.register(CustomUser, CustomUserAdmin)
