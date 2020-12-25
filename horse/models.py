from django.db import models
import datetime

# Create your models here.
from user.models import Owner


class Stable(models.Model):
    number = models.IntegerField()  # validation

    def __str__(self):
        return f'number: {self.number}'

    class Meta:
        db_table = 'stables'


class Horse(models.Model):
    nickname = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner, related_name='horses', on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'horses'


class Photo(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=100)  # URLField?
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'photos'


class StableOccupancy(models.Model):
    day = models.DateTimeField('''default=datetime.datetime.now()''')
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    stable = models.ForeignKey(Stable, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.horse.nickname} on {self.day} in {self.stable.number}'

    class Meta:
        db_table = 'stables_occupancy'
