from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, LogoutView

app_name = 'userprofile'

urlpatterns = [
    path('sign-up/', views.signup, name='signup'),
    path('log-in/', LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out/', LogoutView.as_view(next_page='core:index'), name='logout'),
]