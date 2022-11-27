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
    def validate_name(self, name):
        name = name.title()
        return name

    def validate_surname(self, surname):
        surname = surname.title()
        return surname

    def validate_phoneNumber(self, phoneNumber):
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        if len(phoneNumber) < 9:
            raise serializers.ValidationError('Numer telefonu powinien mieć 9 cyfr')
        else:
            if phoneNumber[0] != '0':
                for char in phoneNumber:
                    if char not in numbers:
                        raise serializers.ValidationError('Niepoprawny numer telefonu')
            else:
                raise serializers.ValidationError('Niepoprawny numer telefonu')
        return phoneNumber

    def validate_pesel(self, pesel):
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        if len(pesel) < 11:
            raise serializers.ValidationError('Pesel powinien mieć 11 cyfr')
        else:
            for char in pesel:
                if char not in numbers:
                    raise serializers.ValidationError('Niepoprawny pesel')
        return pesel

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