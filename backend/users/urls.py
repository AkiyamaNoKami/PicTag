from django.urls import path

from .views import RegistrationView, LogInView, LogOutView, ProfileView

app_name = 'users'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]