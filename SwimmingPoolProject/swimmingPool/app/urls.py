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

    path('api/workers/', views.WorkerList.as_view(), name=views.WorkerList.name),
    path('api/workers/<int:pk>', views.WorkerDetail.as_view(), name=views.WorkerDetail.name),
    path('api/workerAddresses/', views.WorkerAddressList.as_view(), name=views.WorkerAddressList.name),
    path('api/workerAddresses/<int:pk>', views.WorkerAddressDetail.as_view(), name=views.WorkerAddressDetail.name),
    path('api/shifts/', views.ShiftList.as_view(), name=views.ShiftList.name),
    path('api/shifts/<int:pk>', views.ShiftDetail.as_view(), name=views.ShiftDetail.name),
    path('api/tickets/', views.TicketList.as_view(), name=views.TicketList.name),
    path('api/tickets/<int:pk>', views.TicketDetail.as_view(), name=views.TicketDetail.name),
    path('api/clients/', views.ClientList.as_view(), name=views.ClientList.name),
    path('api/clients/<int:pk>', views.ClientDetail.as_view(), name=views.ClientDetail.name),
    path('api/clientAddresses/', views.ClientAddressList.as_view(), name=views.ClientAddressList.name),
    path('api/clientAddresses/<int:pk>', views.ClientAddressDetail.as_view(), name=views.ClientAddressDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),


    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
