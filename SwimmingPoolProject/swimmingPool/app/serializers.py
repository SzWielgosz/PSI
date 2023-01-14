from rest_framework.validators import UniqueValidator

from .models import *
from rest_framework import serializers


class WorkerAddressSerializer(serializers.ModelSerializer):

    # worker = serializers.SlugRelatedField(
    #     queryset=Worker.objects.all(),
    #     slug_field='slugField',
    #     validators=[UniqueValidator(queryset=Ticket.objects.all())]
    # )
    worker = serializers.HyperlinkedRelatedField(view_name='worker-detail', read_only=True)

    class Meta:
        model = WorkerAddress
        fields = ['worker',
                  'street',
                  'houseNumber',
                  'flatNumber',
                  'postcode',
                  'placeName',
                  'url']

    def validate_houseNumber(self, number):
        if number < 0:
            raise serializers.ValidationError("Numer nie moze byc ujemny!")
        return number

    def validate_flatNumber(self, number):
        if number < 0:
            raise serializers.ValidationError("Numer nie moze byc ujemny!")
        return number


class WorkerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Worker
        fields = ['id',
                  'name',
                  'surname',
                  'phoneNumber',
                  'email',
                  'pesel',
                  'url',]

    def validate_name(self, name):
        return name.title()

    def validate_surname(self, surname):
        return surname.title()

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
    # worker = serializers.SlugRelatedField(
    #     queryset=Worker.objects.all(),
    #     slug_field='slugField',
    #     validators=[UniqueValidator(queryset=Shift.objects.all())]
    # )

    worker = serializers.HyperlinkedRelatedField(view_name='worker-detail', read_only=True)

    class Meta:
        model = Shift
        fields = ['worker',
                  'startTime',
                  'endTime',
                  'description',
                  'url']

    def validate(self, data):
        startTime = data['startTime']
        endTime = data['endTime']

        if startTime == endTime:
            raise serializers.ValidationError('Data początku nie może być datą zakończenia')
        if startTime > endTime:
            raise serializers.ValidationError('Data początku jest późniejsza niż rozpoczęcia')
        return data


class ClientSerializer(serializers.ModelSerializer):

    tickets = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='ticket-detail'
    )

    class Meta:
        model = Client
        fields = ['id',
                  'name',
                  'surname',
                  'phoneNumber',
                  'email',
                  'pesel',
                  'url',
                  'tickets']

    def validate_name(self, name):
        return name.title()

    def validate_surname(self, surname):
        return surname.title()

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


class ClientAddressSerializer(serializers.ModelSerializer):
    client = serializers.HyperlinkedRelatedField(view_name='client-detail', read_only=True)

    # client = serializers.SlugRelatedField(
    #     queryset=Client.objects.all(),
    #     slug_field='slugField',
    #     validators=[UniqueValidator(queryset=Ticket.objects.all())]
    # )

    class Meta:
        model = ClientAddress
        fields = ['client',
                  'street',
                  'houseNumber',
                  'flatNumber',
                  'postcode',
                  'placeName',
                  'url']

    def validate_houseNumber(self, number):
        if number < 0:
            raise serializers.ValidationError("Numer nie moze byc ujemny!")
        return number

    def validate_flatNumber(self, number):
        if number < 0:
            raise serializers.ValidationError("Numer nie moze byc ujemny!")
        return number


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    # client = serializers.SlugRelatedField(
    #     queryset=Client.objects.all(),
    #     slug_field='slugField',
    #     validators=[UniqueValidator(queryset=Ticket.objects.all())]
    # )
    #
    # worker = serializers.SlugRelatedField(
    #     queryset=Worker.objects.all(),
    #     slug_field='slugField',
    #     validators=[UniqueValidator(queryset=Ticket.objects.all())]
    # )
    worker = serializers.HyperlinkedRelatedField(view_name='worker-detail', read_only=True)
    client = serializers.HyperlinkedRelatedField(view_name='client-detail', read_only=True)


    class Meta:
        model = Ticket
        fields = [
            'worker',
            'client',
            'price',
            'zone',
            'dateOfPurchase',
            'dateOfEnd',
            'url',
        ]

    def validate(self, data):
        endDate = data['dateOfEnd']
        startTime = data['dateOfPurchase']
        if endDate == startTime:
            raise serializers.ValidationError('Data zakończenia taka sama jak zakupu')
        if endDate < startTime:
            raise  serializers.ValidationError('Data zakończenia wcześniejsza niż zakupu')
        return data

    def validate_price(self, price):
        price = str(price)
        if len(price.rsplit('.')[-1]) > 2:
            raise serializers.ValidationError("Cena nie moze miec wiecej niz 2 miejsca po przecinku")
        price = float(price)
        if price < 0:
            raise serializers.ValidationError("Cena nie moze byc ujemna")
        return price


