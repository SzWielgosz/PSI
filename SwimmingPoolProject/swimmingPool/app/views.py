from django.shortcuts import render
from django.http import HttpResponse
from .models import WorkerAddress, Worker, Shift, ShiftAssignment
from rest_framework import viewsets
from .serializers import WorkerAddressSerializer, WorkerSerializer, ShiftSerializer, ShiftAssigmentSerializer

def index(request):
    return HttpResponse("<h1>Default_view</h1>")


class WorkerAddressViewSet(viewsets.ModelViewSet):
    queryset = WorkerAddress.objects.all()
    serializer_class = WorkerAddressSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


class ShiftAssigmentViewSet(viewsets.ModelViewSet):
    queryset = ShiftAssignment.objects.all()
    serializer_class = ShiftAssigmentSerializer

