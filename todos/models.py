# todos/models.py
from django.db import models
from django.conf import settings
from routines.models import Routine  # 루틴 모델 임포트

class PriorityChoices(models.TextChoices):
    BLACK = 'BLACK', 'BLACK'
    RED = 'RED', 'RED'
    BLUE = 'BLUE', 'BLUE'
    YELLOW = 'YELLOW', 'YELLOW'

class Todo(models.Model):
    todoId = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    dueDate = models.DateField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    createDate = models.DateTimeField(auto_now_add=True)
    todoImage = models.ImageField(upload_to='todo_images/', blank=True, null=True)

    priority = models.CharField(
        max_length=10,
        choices=PriorityChoices.choices,
        default=PriorityChoices.BLACK
    )

    # 새로 추가: routine FK
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.priority}"
