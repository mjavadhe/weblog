from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return '{}.{}'.format(self.pk, self.title)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()


class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=50)
