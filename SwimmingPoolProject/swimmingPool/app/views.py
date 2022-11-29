from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework import viewsets
from .serializers import *

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


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientAdressViewSet(viewsets.ModelViewSet):
    queryset = ClientAdress.objects.all()
    serializer_class = ClientAdressSerializer
