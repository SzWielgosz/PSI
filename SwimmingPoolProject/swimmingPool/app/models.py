from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=45, null=False)
    surname = models.CharField(max_length=45, null=False)
    phoneNumber = models.IntegerField(max_length=9, null=False)
    email = models.CharField(max_length=100)
    pesel = models.IntegerField(max_length=11, null=False)


class WorkerAddress(models.Model):
    street = models.CharField(max_length=45, null=False)
    houseNumber = models.IntegerField(max_length=3, null=False)
    flatNumber = models.IntegerField(max_length=3)
    postcode = models.IntegerField(max_length=45, null=False)
    placeName = models.CharField(max_length=45, null=False)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, default=1)


class Shift(models.Model):
    startTime = models.DateTimeField(null=False)
    endTime = models.DateTimeField(null=False)
    description = models.CharField(max_length=255)


class ShiftAssignment(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)


class Ticket(models.Model):
    price = models.FloatField(null=False)
    zone = models.CharField(max_length=45, null=False)
    dateOfPurchase = models.DateTimeField(null=False)
    dateOfEnd = models.DateTimeField(null=False)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)


class ClientAdress(models.Model):
    street = models.CharField(max_length=45, null=False)
    houseNumber = models.IntegerField(max_length=3, null=False)
    flatNumber = models.IntegerField(max_length=3)
    postcode = models.CharField(max_length=11, null=False)
    placeName = models.CharField(max_length=45, null=False)


class Client(models.Model):
    name = models.CharField(max_length=45, null=False)
    surname = models.CharField(max_length=45, null=False)
    phoneNumber = models.IntegerField(max_length=9, null=False)
    email = models.CharField(max_length=100)
    pesel = models.IntegerField(max_length=11, null=False)
    adress = models.ForeignKey(ClientAdress, on_delete=models.CASCADE)


class TicketAssignment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
