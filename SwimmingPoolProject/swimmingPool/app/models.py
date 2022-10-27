from django.db import models


class WorkerAddress(models.Model):
    street = models.CharField(max_length=45, null=False)
    houseNumber = models.IntegerField(3, null=False)
    flatNumber = models.IntegerField(3)
    postcode = models.IntegerField(45, null=False)
    placeName = models.CharField(max_length=45, null=False)


class Worker(models.Model):
    name = models.CharField(max_length=45, null=False)
    surname = models.CharField(max_length=45, null=False)
    phoneNumber = models.IntegerField(max_length=9, null=False)
    email = models.CharField(100)
    pesel = models.IntegerField(9)
    idAdres = models.ForeignKey(WorkerAddress, on_delete=models.CASCADE)


class Shift(models.Model):
    startTime = models.DateTimeField(null=False)
    endTime = models.DateTimeField(null=False)
    description = models.CharField(255)


class ShiftAssignment(models.Model):
    idWorker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    idShift = models.ForeignKey(Shift, on_delete=models.CASCADE)
