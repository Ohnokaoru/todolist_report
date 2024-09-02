from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate

# Create your views here.


# 註冊(使用內建UserCreationForm表單)
def user_register(request):
    message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        # 會自動驗證表單內容，若無誤就建立表單
        if form.is_valid():
            form.save()
            message = "註冊成功"

        else:
            message = "資料錯誤:"

    else:
        form = UserCreationForm()

    return render(
        request, "user/user-register.html", {"message": message, "form": form}
    )


# 登入，直接除理表單(抓取欄位)
def user_login(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            message = "登入成功"

        else:
            message = "資料錯誤"

    return render(request, "user-login.html", {"message": message})
