from django.shortcuts import render
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import TodoForm


# Create your views here.


# 新增待辦事項
@login_required
def create_todo(request):
    message = ""
    todoform = ""

    if request.method == "POST":
        try:
            form = TodoForm(request.POST)
            todoform = form.save(commit=False)
            todoform.user = request.user
            todoform.save()
            message = "新增成功"

        except Exception as e:
            message = f"錯誤:{e}"

    else:
        form = TodoForm()

    return render(
        request,
        "todo/create-todo.html",
        {"form": form, "todoform": todoform, "message": message},
    )
