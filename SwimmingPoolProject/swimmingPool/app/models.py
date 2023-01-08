import datetime
from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=45, null=False)
    surname = models.CharField(max_length=45, null=False)
    phoneNumber = models.CharField(max_length=9, null=False)
    email = models.EmailField(null=True)
    pesel = models.CharField(max_length=11, null=False)

    def __str__(self):
        return f'{self.name} {self.surname}'


class WorkerAddress(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, default=None)
    street = models.CharField(max_length=45, null=False)
    houseNumber = models.IntegerField(null=False)
    flatNumber = models.IntegerField(null=True)
    postcode = models.CharField(max_length=11, null=False)
    placeName = models.CharField(max_length=45, null=False)

    def __str__(self):
        return f'{self.worker}'


SHIFTS_CHOICES = (
    ("FIRST_SHIFT", "1 zmiana"),
    ("SECOND_SHIFT", "2 zmiana")
)


class Shift(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, default=None)
    startTime = models.DateTimeField(null=False)
    endTime = models.DateTimeField(null=False)
    description = models.CharField(max_length=12, choices=SHIFTS_CHOICES)

    def __str__(self):
        return self.description

class Client(models.Model):
    name = models.CharField(max_length=45, null=False)
    surname = models.CharField(max_length=45, null=False)
    phoneNumber = models.CharField(max_length=9, null=False)
    email = models.EmailField(null=True)
    pesel = models.CharField(max_length=11, null=False)

    def __str__(self):
        return f'{self.name} {self.surname}'


class ClientAddress(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    street = models.CharField(max_length=45, null=False)
    houseNumber = models.IntegerField(null=False)
    flatNumber = models.IntegerField(null=True)
    postcode = models.CharField(max_length=11, null=False)
    placeName = models.CharField(max_length=45, null=False)

    def __str__(self):
        return f'{self.client}'

class Ticket(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.SET_DEFAULT, default=None)
    client = models.ForeignKey(Client, on_delete=models.SET_DEFAULT, default=None)
    price = models.FloatField(null=False)
    zone = models.CharField(max_length=45, null=False)
    dateOfPurchase = models.DateTimeField(null=False, default=datetime.datetime.now())
    dateOfEnd = models.DateTimeField(null=False)

    def __str__(self):
        return f'{self.client}'
