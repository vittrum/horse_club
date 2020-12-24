from django.db import models


# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=17)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        db_table = 'owners'


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'roles'


class Trainer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=17)
    password_hash = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        db_table = 'trainers'


class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=17)
    password_hash = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        db_table = 'clients'
