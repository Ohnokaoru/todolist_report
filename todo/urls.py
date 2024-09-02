from django.urls import path
from . import views

urlpatterns = [
    path("creat-todo", views.creat_todo, name="creat-todo"),
]
