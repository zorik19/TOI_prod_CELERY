from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_exempt


def users(request):
    return render(request, "users/users.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

