from django.urls import path
from . import views

urlpatterns = [
    path("user-register", views.user_register, name="user-register"),
]
