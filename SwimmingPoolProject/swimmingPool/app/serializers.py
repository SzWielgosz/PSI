from .models import *
from rest_framework import serializers

class WorkerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerAddress
        fields = [
            'street',
            'houseNumber',
            'flatNumber',
            'postcode',
            'placeName',
            'worker'
        ]

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = [
            'name',
            'surname',
            'phoneNumber',
            'email',
            'pesel'
        ]

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = [
            'startTime',
            'endTime',
            'description'
        ]

class ShiftAssigmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftAssignment
        fields = [
            'worker',
            'shift'
        ]

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'price',
            'zone',
            'dateOfPurchase',
            'dateOfEnd',
            'worker'
        ]

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'name',
            'surname',
            'phoneNumber',
            'email',
            'pesel'
        ]

class ClientAdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAdress
        fields = [
            'street',
            'houseNumber',
            'flatNumber',
            'postcode',
            'placeName',
            'client'
        ]

class TicketAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'ticket',
            'client'
        ]