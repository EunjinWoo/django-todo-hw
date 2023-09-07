# tweet/models.py
from django.db import models
from user.models import UserModel


# Create your models here.
class TodoModel(models.Model):
    class Meta:
        db_table = "todo"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)