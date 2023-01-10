from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework import permissions, filters
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins

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


class WorkerGenericAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [permissions.IsAdminUser]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'surname', 'phoneNumber', 'email', 'pesel']
    ordering_fields = ['surname', 'name']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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


class WorkerAddressesGenericAPIView(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = WorkerAddress.objects.all()
    serializer_class = WorkerAddressSerializer
    permission_classes = [permissions.IsAdminUser]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['houseNumber', 'flatNumber', 'postcode', 'placeName']
    ordering_fields = ['worker', 'street', 'placeName']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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


class ShiftsGenericAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [permissions.IsAdminUser]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['startTime', 'endTime', 'description']
    ordering_fields = ['startTime', 'endTime', 'description']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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


class TicketGenericAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAdminUser]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['price', 'zone', 'dateOfPurchase', 'dateOfEnd']
    ordering_fields = ['price', 'dateOfPurchase', 'dateOfEnd']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



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


class ClientsGenericAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'surname', 'phoneNumber', 'email', 'pesel']
    ordering_fields = ['name', 'surname']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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


class ClientAddressesGenericAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressSerializer
    permission_classes = [permissions.IsAdminUser]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['houseNumber', 'flatNumber', 'postcode', 'placeName']
    ordering_fields = ['postcode', 'placeName', 'client', 'street']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
