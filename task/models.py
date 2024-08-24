from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return self.title
