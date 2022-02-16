from django import forms
from todo_app.models import TodoModel, Profile


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


class UpdatePictureProfile(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    website_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ('bio', 'website_url', 'profile_pic')

    def __init__(self, *args, **kwargs):
        super(UpdatePictureProfile, self).__init__(*args, **kwargs)
        self.fields['website_url'].required = False
