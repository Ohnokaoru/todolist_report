from django.contrib import admin
from .models import Todo

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "important",
        "create_time",
        "completed",
        "completed_time",
    )
    list_filter = ("important", "completed")
    search_fields = ("id", "title")
    ordering = ("-create_time",)


admin.site.register(Todo, TodoAdmin)
