from django.db import models
from django.contrib.auth.models import User


class Module(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=40, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class BaseTodo(models.Model):
    text = models.CharField(max_length=300)
    is_done = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class LectureTodo(BaseTodo):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    duration = models.PositiveSmallIntegerField(blank=True)
