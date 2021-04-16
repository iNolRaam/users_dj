from django.urls import path

from . import views

app_name = 'home_app'

urlpatterns = [
    path('home/index/', 
         views.HomePage.as_view(),
         name='home'),
]