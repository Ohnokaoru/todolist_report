from django.urls import path
from . import views

urlpatterns = [
    path("create-todo/", views.create_todo, name="create-todo"),
    path("all-todo/", views.all_todo, name="all-todo"),
]
