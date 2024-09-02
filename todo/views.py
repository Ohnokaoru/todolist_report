from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import TodoForm
import math


# Create your views here.


# 新增待辦事項
@login_required
def create_todo(request):
    message = ""

    if request.method == "POST":
        try:
            form = TodoForm(request.POST)
            todoform = form.save(commit=False)
            todoform.user = request.user
            todoform.save()
            return redirect("all-todo")

        except Exception as e:
            message = f"錯誤:{e}"

    else:
        form = TodoForm()

    return render(
        request,
        "todo/create-todo.html",
        {"form": form, "message": message},
    )


# 檢查所有自己的待辦事項(頁數)
@login_required
def all_todo(request):
    message = ""
    todos = Todo.objects.all()
    if not todos:
        message = "沒有待辦事項"

    else:
        # 頁數預設為1
        page = int(request.GET.get("page", 1))
        # 切換上下頁預設為空
        page_btn = request.GET.get("page_btn", "")

        total_todo = len(todos)
        page_size = 3
        total_page = math.ceil(total_todo / page_size)

        # 合理頁數
        if page > total_page:
            page = total_page

        if page < 1:
            page = 1

        # 點擊上頁
        if page_btn == "prev" and page > 1:
            page -= 1

        # 點擊下頁
        if page_btn == "next" and page < total_page:
            page += 1

        # 計算一頁的資料
        start = (page - 1) * page_size
        end = start + page_size
        todos = Todo.objects.all().order_by("-create_time")[start:end]

        next = page < total_page
        prev = page > 1

        return render(
            request,
            "todo/all-todo.html",
            {
                "page": page,
                "total_page": total_page,
                "todos": todos,
                "next": next,
                "prev": prev,
            },
        )


# 詳細內文
@login_required
def todo_detail(request, todo_id):
    try:
        todo = Todo.objects.get(user=request.user, id=todo_id)

    except Todo.DoesNotExist:
        return redirect("all-todo")

    return render(request, "todo/todo-detail.html", {"todo": todo})
