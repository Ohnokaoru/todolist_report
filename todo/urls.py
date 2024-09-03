from django.urls import path
from . import views

urlpatterns = [
    path("create-todo/", views.create_todo, name="create-todo"),
    path("all-todo/", views.all_todo, name="all-todo"),
    path("todo-detail/<int:todo_id>/", views.todo_detail, name="todo-detail"),
    path("edit-todo/<int:todo_id>/", views.edit_todo, name="edit-todo"),
    path("uncompleted-todo/", views.uncompleted_todo, name="uncompleted-todo"),
    path("completed-todo/", views.completed_todo, name="completed-todo"),
    path("delete-todo/<int:todo_id>", views.delete_todo, name="delete-todo"),
]
