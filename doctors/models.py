from django.db import models


class Direction(models.Model):
    direction_name = models.CharField(max_length=150)
    slag = models.SlugField(null=True)

    def __str__(self):
        return self.direction_name


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=150)
    slag = models.SlugField(null=True)
    direction = models.ManyToManyField(Direction,
                                       )
    description = models.TextField()
    date_of_birthday = models.DateField()
    experience = models.IntegerField()

    def __str__(self):
        return self.doctor_name
