from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework import permissions
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


def index(request):
    return HttpResponse("<h1>Default_view</h1>")


class WorkerAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        names = [worker.name for worker in Worker.objects.all()]
        return Response(names)


class WorkerAddressAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        addresses = [workerAddress.street for workerAddress in WorkerAddress.objects.all()]
        return Response(addresses)


class ShiftAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        shifts = [shift.description for shift in Shift.objects.all()]
        return Response(shifts)
#
#
class TicketAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        tickets = [ticket.zone for ticket in Ticket.objects.all()]
        return Response(tickets)
#
#
class ClientAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        names = [client.name for client in Client.objects.all()]
        return Response(names)
#
#
class ClientAddressAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        addresses = [clientAddress.street for clientAddress in ClientAddress.objects.all()]
        return Response(addresses)
