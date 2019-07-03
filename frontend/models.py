from django.db import models


class Passanger(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    survived = models.BooleanField()
    age = models.FloatField()
    ticket_class = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=255)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
