from .models import Todo
from django.contrib.auth import forms


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ("user",)
