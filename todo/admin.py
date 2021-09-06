from django.contrib import admin

# Register your models here.
from todo.models import TodoList


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    pass