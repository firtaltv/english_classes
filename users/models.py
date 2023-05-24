from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Status(models.TextChoices):
        Teacher = 'Teacher', _('Teacher'),
        Student = 'Student', _('Student'),

    age = models.IntegerField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.Teacher,
    )

    # def __str__(self):
    #     return self.name
