from django.db import models
from django.urls import reverse


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # description = models.RichText()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('list_todos')
