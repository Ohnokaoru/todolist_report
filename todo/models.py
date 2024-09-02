from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50, default="")
    text = models.TextField(blank="", default="")
    important = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    completed_time = models.DateTimeField(blank="", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.important} {self.completed_time}"
