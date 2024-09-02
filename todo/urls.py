from django.urls import path
from . import views

urlpatterns = [
    path("create-todo/", views.create_todo, name="create-todo"),
    path("all-todo/", views.all_todo, name="all-todo"),
    path("", views.all_todo, name="all-todo"),
    path("todo-detail/<int:todo_id>", views.todo_detail, name="todo-detail"),
]
