from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import UserForm


class SignUp(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

