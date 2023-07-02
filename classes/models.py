from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User


class EnglishClass(models.Model):
    class Status(models.TextChoices):
        ToBeDone = 'ToBeDone', _('To be Done')
        InProgress = 'InProgress', _('In Progress')
        Done = 'Done', _('Done')

    class Level(models.TextChoices):
        A1 = 'A1', _('A1')
        A2 = 'A2', _('A2')
        B1 = 'B1', _('B1')
        B2 = 'B2', _('B2')
        C1 = 'C1', _('C1')
        C2 = 'C2', _('C2')
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')
    students = models.ManyToManyField(User, related_name='students')
    level = models.CharField(
        max_length=5,
        choices=Level.choices,
        default=Level.A1
    )
    eventId = models.CharField(max_length=256)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ToBeDone,
    )

    def __str__(self):
        return str(self.date)
