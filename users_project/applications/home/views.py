import datetime

from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    TemplateView
)
# Create your views here.


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "home/index.html"
    login_url = reverse_lazy('users_app:login')
