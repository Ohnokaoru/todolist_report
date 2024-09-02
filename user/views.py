from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


# 註冊(使用內建UserCreationForm表單)
def user_register(request):
    message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        # 會自動驗證表單內容，若無誤就建立表單
        if form.is_valid():
            form.save()

        else:
            message = "資料錯誤:"

    else:
        form = UserCreationForm()

    return render(
        request, "user/user-register.html", {"message": message, "form": form}
    )
