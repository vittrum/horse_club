from django.db import models
import datetime

# Create your models here.
from horse.models import Horse
from user.models import Client, Trainer


class Discipline(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()  # validation

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'disciplines'


class Plan(models.Model):
    amount = models.CharField(max_length=50)  # validation
    discount = models.IntegerField()  # validation

    def __str__(self):
        return f'am: {self.amount} disc: {self.discount}'

    class Meta:
        db_table = 'plans'


class Subscription(models.Model):
    name = models.CharField(max_length=50)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subscriptions'


class ClientSubscriptions(models.Model):
    purchase_date = models.DateTimeField('''default=datetime.datetime.now()''')
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    available_lessons = models.IntegerField()

    def __str__(self):
        return f'{self.subscription.name} of {self.client.__str__()}'

    class Meta:
        db_table = 'clients_subscriptions'


class Schedule(models.Model):
    date = models.DateTimeField()
    begin_time = models.TimeField()
    end_time = models.TimeField(null=True)
    client_subscription = models.ForeignKey(ClientSubscriptions, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} with {self.trainer.__str__()} and {self.horse.nickname}'

    class Meta:
        db_table = 'schedules'
