from django.db import models
from django.contrib.auth.models import AbstractUser

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return '{}.{}'.format(self.pk, self.title)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()


"""class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # تغییر related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # تغییر related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )"""


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)  # Ezafe kardan is_active field
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Taghir related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Taghir related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )