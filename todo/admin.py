from django.contrib import admin

# Register your models here.
from todo.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['todo_title', 'todo_deadline_date']

