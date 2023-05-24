from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone



class Profile(models.Model):
    class Status(models.TextChoices):
        Teacher = 'Teacher', _('Teacher'),
        Student = 'Student', _('Student'),

    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    date_registration = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.Teacher,
    )
    def __str__(self):
        return self.name
