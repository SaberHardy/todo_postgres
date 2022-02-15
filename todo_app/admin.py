from django.contrib import admin

from todo_app.models import TodoModel


# admin.site.register(TodoModel)

@admin.register(TodoModel)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'date_created')
