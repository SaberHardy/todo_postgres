from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # description = models.RichText()
    date_created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('list_todos')