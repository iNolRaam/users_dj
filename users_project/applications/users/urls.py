from django.urls import path

from . import views

app_name = 'users_app'

urlpatterns = [
    path('register/', 
         views.RegisterUserView.as_view(),
         name='register_user'),
     path('login/', 
         views.LoginView.as_view(),
         name='login'),
     
      path('logout/', 
         views.LogoutView.as_view(),
         name='logout'),
]