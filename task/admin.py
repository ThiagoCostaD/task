from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'completed', 'created_at', 'due_date', 'user']
    search_fields = ['title', 'description']
    list_filter = ['completed', 'due_date', 'user']


admin.site.register(Task, TaskAdmin)
