from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=30, unique=True, blank=True, null=True)
    createDate = models.DateTimeField(auto_now_add=True)  # 가입일 필드 추가

    def __str__(self):
        return self.username
