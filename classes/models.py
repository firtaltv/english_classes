from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User


class EnglishClass(models.Model):
    class Status(models.TextChoices):
        ToBeDone = 'ToBeDone', _('To be Done')
        InProgress = 'InProgress', _('In Progress')
        Done = 'Done', _('Done')
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')
    students = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students')
    eventId = models.CharField(max_length=256)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ToBeDone,
    )
