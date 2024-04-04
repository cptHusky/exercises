from django.db import models

from exercises_app.constants import LEVEL_CHOICES, TYPE_CHOICES


class Exercise(models.Model):
    name = models.CharField(max_length=24)
    description = models.TextField()
    type = models.CharField(max_length=12, choices=TYPE_CHOICES)
    level = models.CharField(max_length=12, choices=LEVEL_CHOICES)
    duration = models.DurationField()
    reps = models.IntegerField()
    sets = models.IntegerField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
