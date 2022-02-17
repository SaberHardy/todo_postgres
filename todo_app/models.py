from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    # description = models.TextField()
    description = RichTextField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='todo_app')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('list_todos')

    def total_likes(self):
        return self.likes.count()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/', null=True, blank=True, default='images/default.png')
    website_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('list_todos')


class Comment(models.Model):
    todo = models.ForeignKey(TodoModel, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
