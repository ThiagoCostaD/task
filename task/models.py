from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name='Título'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição'
    )
    completed = models.BooleanField(
        default=False,
        verbose_name='Concluída'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criada em',
        editable=False,
        blank=True,
        null=True,
    )
    due_date = models.DateField(
        verbose_name='Data de vencimento',
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        User,
        related_name='tasks',
        on_delete=models.CASCADE,
        verbose_name='Usuário',
    )

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return self.title
