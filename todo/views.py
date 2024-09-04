from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import TodoForm
import math
from django.utils import timezone
from django.core.paginator import Paginator


# Create your views here.


# 新增待辦事項
@login_required
def create_todo(request):
    message = ""

    if request.method == "POST":
        try:
            form = TodoForm(request.POST)
            todoform = form.save(commit=False)
            # completed_time為空，所以目前不需要驗證
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

    todos = Todo.objects.filter(user=request.user).order_by("-create_time")
    if not todos:
        return redirect("create-todo")

    else:

        # 分頁器(object_list,一頁多少筆)
        paginator = Paginator(todos, 3)
        # 若為None給1
        try:
            page_number = int(request.GET.get("page", 1))

        except (TypeError, ValueError):
            page_number = 1

        # 計算合理頁數，並取得頁碼(第一頁與與總共多少頁)
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "todo/all-todo.html",
            {"page_obj": page_obj},
        )


# 詳細內文
@login_required
def todo_detail(request, todo_id):
    try:
        todo = Todo.objects.get(user=request.user, id=todo_id)

    except Todo.DoesNotExist:
        return redirect("all-todo")

    return render(request, "todo/todo-detail.html", {"todo": todo})


# 修改待辦事項
@login_required
def edit_todo(request, todo_id):
    message = ""
    try:
        todo = Todo.objects.get(user=request.user, id=todo_id)
    except Todo.DoesNotExist:
        return redirect("all-todo")

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            todoform = form.save(commit=False)
            todoform.user = request.user
            if todoform.completed:
                todoform.completed_time = timezone.now()

            todoform.save()
            return redirect("todo-detail", todo_id=todo.id)

        else:
            message = "資料錯誤"

    else:
        form = TodoForm(instance=todo)

    return render(
        request,
        "todo/edit-todo.html",
        {"message": message, "form": form, "todo": todo},
    )


# 選取完成待辦事項
@login_required
def uncompleted_todo(request):
    message = ""
    uncompleted_todos = Todo.objects.filter(
        user=request.user, completed=False
    ).order_by("-create_time")

    if not uncompleted_todos:
        return redirect("all-todo")

    else:
        paginator = Paginator(uncompleted_todos, 3)

        try:
            page_number = int(request.GET.get("page", 1))

        except (TypeError, ValueError):
            page_number = 1

        page_obj = paginator.get_page(page_number)

        return render(request, "todo/uncompleted-todo.html", {"page_obj": page_obj})


# 選取完成待辦事項
@login_required
def completed_todo(request):
    completed_todos = Todo.objects.filter(user=request.user, completed=True).order_by(
        "-create_time"
    )
    message = ""
    if completed_todos:
        total_completed = len(completed_todos)
        page = int(request.GET.get("page", 1))
        page_size = 3
        total_page = math.ceil(total_completed / page_size)
        page_btn = request.GET.get("page_btn", "")

        # 合理頁數
        if page > total_page:
            page = total_page

        if page < 1:
            page = 1

        # 點擊上一頁
        if page_btn == "prev" and page > 1:
            page -= 1

        # 點擊下一頁
        if page_btn == "next" and page < total_page:
            page += 1

        # 計算一頁的筆數
        start = (page - 1) * page_size
        end = start + page_size
        completed_todos = Todo.objects.filter(
            user=request.user, completed=True
        ).order_by("-create_time")[start:end]

        next = page < total_page
        prev = page > 1

    else:
        message = "沒有已完成的待辦事項"

    return render(
        request,
        "todo/completed-todo.html",
        {
            "page": page,
            "total_page": range(1, total_page + 1),
            "completed_todos": completed_todos,
            "next": next,
            "prev": prev,
            "message": message,
        },
    )


# 刪除待辦事項
@login_required
def delete_todo(request, todo_id):
    delete_todo = ""

    try:
        delete_todo = Todo.objects.get(user=request.user, id=todo_id)

    except Todo.DoesNotExist:
        return redirect("all-todo")

    if request.method == "POST":
        delete_btn = request.POST.get("delete_btn")
        delete_todo.delete()
        return redirect("all-todo")

    return render(request, "todo/delete-todo.html", {"delete_todo": delete_todo})
