from django.urls import path
from .views import signup

from django.contrib.auth import views

app_name = 'userprofile'

urlpatterns = [
    path('sign-up/', signup, name='signup'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login')
]