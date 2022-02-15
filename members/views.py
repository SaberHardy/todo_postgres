from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from members.forms import RegisterForm


class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
