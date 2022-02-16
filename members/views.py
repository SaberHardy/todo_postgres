from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy

from members.forms import RegisterForm, UpdateProfileForm


class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class EditUserForm(generic.UpdateView):
    form_class = UpdateProfileForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('list_todos')

    def get_object(self, **kwargs):
        return self.request.user

