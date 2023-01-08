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

    def post(self, request):
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WorkerAddressAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        addresses = WorkerAddress.objects.all()
        serializer = WorkerAddressSerializer(addresses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WorkerAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ShiftAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        shifts = Shift.objects.all()
        serializer = WorkerAddressSerializer(shifts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class TicketAPIView(APIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ClientAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ClientAddressAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        addresses = ClientAddress.objects.all()
        serializer = ClientAddressSerializer(addresses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
