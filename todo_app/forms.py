from django import forms
from todo_app.models import TodoModel


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ('title', 'description',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Enter your task title'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter your task description'})
        }
