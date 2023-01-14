from .models import *
from rest_framework import serializers


class WorkerAddressSerializer(serializers.ModelSerializer):

    # worker = serializers.SlugRelatedField(
    #     queryset=Worker.objects.all(),
    #     slug_field='slugField',
    #     validators=[UniqueValidator(queryset=Ticket.objects.all())]
    # )
    worker = serializers.HyperlinkedRelatedField(view_name='worker-detail', read_only=False, queryset=Worker.objects.all())

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

    worker = serializers.HyperlinkedRelatedField(view_name='worker-detail', read_only=False, queryset=Worker.objects.all())

    startTime = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S%z')

    class Meta:
        model = Shift
        fields = ['id',
                  'worker',
                  'startTime',
                  'endTime',
                  'description',
                  'url']

    def validate(self, data):
        startTime = data['startTime']
        start = startTime.strftime('%Y-%m-%dT%H:%M:%S%z')
        now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z')

        if start < now:
            raise serializers.ValidationError('Data początku musi byc data terazniejsza lub przyszla')

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
    client = serializers.HyperlinkedRelatedField(view_name='client-detail', read_only=False, queryset=Client.objects.all())

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

    worker = serializers.HyperlinkedRelatedField(view_name='worker-detail', read_only=False, queryset=Worker.objects.all())
    client = serializers.HyperlinkedRelatedField(view_name='client-detail', read_only=False, queryset=Client.objects.all())


    class Meta:
        model = Ticket
        fields = [
            'worker',
            'client',
            'dateOfPurchase',
            'dateOfEnd',
            'price',
            'zone',
            'url',
        ]


    def validate_price(self, price):
        price = str(price)
        if len(price.rsplit('.')[-1]) > 2:
            raise serializers.ValidationError("Cena nie moze miec wiecej niz 2 miejsca po przecinku")
        price = float(price)
        if price < 0:
            raise serializers.ValidationError("Cena nie moze byc ujemna")
        return price
