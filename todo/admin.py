from django.contrib import admin

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "important", "create_time", "completed_time")
    list_filter = ("important",)
    search_fields = ("id", "title")
    ordering = ("-create_time",)
