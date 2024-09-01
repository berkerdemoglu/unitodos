from django.db import models
from django.contrib.auth.models import User


class Module(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=40, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.code == '':
            return self.name
        else:
            return f'{self.code}: {self.name}'

    class Meta:
        unique_together = ['id', 'owner']


class BaseTodo(models.Model):
    is_done = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class LectureTodo(BaseTodo):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    topic = models.CharField(max_length=120, blank=True)
    lecture_date = models.DateField(blank=True, null=True)
    duration = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        if self.topic == '' and self.lecture_date is None:
            return f'{self.module.name} | Lecture {self.id}'
        elif self.topic == '' and self.lecture_date is not None:
            return f'Lecture from {self.lecture_date}'
        elif self.topic != '' and self.lecture_date is None:
            return f'Lecture on {self.topic}'
        else:
            return f'{self.topic}: {self.lecture_date}'

    @property
    def as_module_and_id(self):
        if self.module.code != '':
            return f'{self.module.code} | Lecture {self.id}'
        else:
            return f'{self.module.name} | Lecture {self.id}'
