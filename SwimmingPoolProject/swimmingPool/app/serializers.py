from .models import WorkerAddress, Worker, Shift, ShiftAssignment
from rest_framework import serializers

class WorkerAddressSerializer(serializers.HyperlinkedModelSerializer):
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

class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Worker
        fields = [
            'name',
            'surname',
            'phoneNumber',
            'email',
            'pesel'
        ]

class ShiftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shift
        fields = [
            'startTime',
            'endTime',
            'description'
        ]

class ShiftAssigmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShiftAssignment
        fields = [
            'worker',
            'shift'
        ]