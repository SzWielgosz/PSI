"""swimmingPool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),

    path('api/workers/', views.WorkerAPIView.as_view(), name='worker'),
    path('api/workerAddresses/', views.WorkerAddressAPIView.as_view(), name='workerAddresses'),
    path('api/shifts/', views.ShiftAPIView.as_view(), name='shifts'),
    path('api/tickets/', views.TicketAPIView.as_view(), name='tickets'),
    path('api/clients/', views.ClientAPIView.as_view(), name='clients'),
    path('api/clientAddresses/', views.ClientAddressAPIView.as_view(), name='clientAddresses'),

    path('api/ticketsGeneric/', views.TicketGenericAPIView.as_view(), name='ticketsGenericList'),
    path('api/workersGeneric/', views.WorkerGenericAPIView.as_view(), name='workersGenericList'),
    path('api/workerAddressesGeneric/', views.WorkerAddressesGenericAPIView.as_view(), name='workerAddressesGenericList'),
    path('api/shiftsGeneric/', views.ShiftsGenericAPIView.as_view(), name='shiftsGenericList'),
    path('api/clientsGeneric/', views.ClientsGenericAPIView.as_view(), name='clientsGenericList'),
    path('api/clientAddressesGeneric/', views.ClientAddressesGenericAPIView.as_view(), name='clientAddressesGenericList'),

    path('api/shiftsFilter/<str:name>', views.ShiftsFilter.as_view(), name='shiftFilter'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
