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

    def get(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)


class WorkerAddressAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        adresses = WorkerAddress.objects.all()
        serializer = WorkerAddressSerializer(adresses, many=True)
        return Response(serializer.data)


class ShiftAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        shifts = Shift.objects.all()
        serializer = WorkerAddressSerializer(shifts, many=True)
        return Response(serializer.data)


class TicketAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)


class ClientAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)


class ClientAddressAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        adresses = ClientAddress.objects.all()
        serializer = ClientAddressSerializer(adresses, many=True)
        return Response(serializer.data)
