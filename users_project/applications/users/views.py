from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from django.views.generic.edit import (
    View,
    FormView
)

from .forms import RegisterUserForm, LoginForm
from .models import User

# Create your views here.

class RegisterUserView(FormView):
    template_name = "users/register.html"
    form_class = RegisterUserForm
    success_url = '/'
    
    def form_valid(self, form):

        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            first_name=form.cleaned_data['first_name'],
            second_name=form.cleaned_data['second_name'],
            first_last_name=form.cleaned_data['first_last_name'],
            second_last_name=form.cleaned_data['second_last_name'],
            gender=form.cleaned_data['gender'],
        )
        
        return super(RegisterUserView, self).form_valid(form)




class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home')
    
    
    def form_valid(self, form):
        
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
        )
        
        login(self.request, user)
        
        return super(LoginView, self).form_valid(form)    

class LogoutView(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        
        return HttpResponseRedirect(
            reverse(
                'users_app:login'
            )
        )
    