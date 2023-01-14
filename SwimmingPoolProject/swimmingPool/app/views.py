from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework import permissions, filters
from .serializers import *
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from .custom_permissions import IsCurrentUserOwnerOrReadOnly
from rest_framework import permissions


def index(request):
    return HttpResponse("<h1>Default_view</h1>")


class WorkerList(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    name = 'worker-list'
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)


class WorkerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    name = 'worker-detail'


class WorkerAddressFilter(FilterSet):
    from_houseNumber = NumberFilter(field_name='houseNumber', lookup_expr='gte')
    to_houseNumber = NumberFilter(field_name='houseNumber', lookup_expr='lte')
    from_flatNumber = NumberFilter(field_name='flatNumber', lookup_expr='gte')
    to_flatNumber = NumberFilter(field_name='flatNumber', lookup_expr='lte')

    class Meta:
        model = WorkerAddress
        fields = ['from_houseNumber', 'to_houseNumber', 'from_flatNumber', 'to_flatNumber']


class WorkerAddressList(generics.ListCreateAPIView):
    queryset = WorkerAddress.objects.all()
    serializer_class = WorkerAddressSerializer
    name = 'workeraddress-list'
    filterset_class = WorkerAddressFilter
    search_fields = ['postcode', 'street']
    ordering_fields = ['phoneNumber']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)


class WorkerAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkerAddress.objects.all()
    name = 'workeraddress-detail'
    serializer_class = WorkerAddressSerializer


class ShiftFilter(FilterSet):
    from_startTime = DateTimeFilter(field_name='startTime', lookup_expr='gte')
    to_startTime = DateTimeFilter(field_name='startTime', lookup_expr='lte')
    from_endTime = DateTimeFilter(field_name='endTime', lookup_expr='gte')
    to_endTime = DateTimeFilter(field_name='endTime', lookup_expr='lte')

    class Meta:
        model = Shift
        fields = ['from_startTime', 'to_startTime', 'from_endTime', 'to_endTime']


class ShiftList(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    name = 'shift-list'
    filterset_class = ShiftFilter
    search_fields = ['worker', 'startTime', 'endTime']
    ordering_fields = ['worker']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)


class ShiftDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    name = "shift-detail"


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filterset_fields = ['name', 'surname', 'phoneNumber']
    search_fields = ['name', 'surname', 'phoneNumber']
    ordering_fields = ['phoneNumber']
    name = 'client-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'


class ClientAddressFilter(FilterSet):
    from_houseNumber = NumberFilter(field_name='houseNumber', lookup_expr='gte')
    to_houseNumber = NumberFilter(field_name='houseNumber', lookup_expr='lte')
    from_flatNumber = NumberFilter(field_name='flatNumber', lookup_expr='gte')
    to_flatNumber = NumberFilter(field_name='flatNumber', lookup_expr='lte')

    class Meta:
        model = ClientAddress
        fields = ['from_houseNumber', 'to_houseNumber', 'from_flatNumber', 'to_flatNumber']


class ClientAddressList(generics.ListCreateAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressSerializer
    name = 'clientaddress-list'
    filterset_class = ClientAddressFilter
    search_fields = ['postcode', 'street']
    ordering_fields = ['phoneNumber']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)


class ClientAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressSerializer
    name = 'clientaddress-detail'


class TicketFilter(FilterSet):
    from_date_purchase = DateTimeFilter(field_name='dateOfPurchase', lookup_expr='gte')
    to_date_purchase = DateTimeFilter(field_name='dateOfPurchase', lookup_expr='lte')
    from_date_end = DateTimeFilter(field_name='dateOfEnd', lookup_expr='gte')
    to_date_end = DateTimeFilter(field_name='dateOfEnd', lookup_expr='lte')
    from_price = NumberFilter(field_name='price', lookup_expr='gte')
    to_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Ticket
        fields = ['from_date_purchase', 'to_date_purchase', 'from_date_end', 'to_date_end', 'from_price', 'to_price']


class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)
    filterset_class = TicketFilter
    name = 'ticket-list'

    search_fields = ['price', 'zone', 'dateOfEnd']
    ordering_fields = ['price', 'zone', 'dateofPurchase', 'dateOfEnd']


class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    name = 'ticket-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'workers': reverse(WorkerList.name, request=request),
                         'workerAddresses': reverse(WorkerAddressList.name, request=request),
                         'shifts': reverse(ShiftList.name, request=request),
                         'clients': reverse(ClientList.name, request=request),
                         'clientAddresses': reverse(ClientAddressList.name, request=request),
                         'tickets': reverse(TicketList.name, request=request)
        })
