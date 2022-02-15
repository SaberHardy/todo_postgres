from django.contrib import admin

from todo_app.models import TodoModel


@admin.register(TodoModel)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created',)
