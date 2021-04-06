from django.urls import path
from .views import RegisterUserView, login

urlpatterns = [
    path('login', login),
    path('register', RegisterUserView.as_view(), name="register")
]

