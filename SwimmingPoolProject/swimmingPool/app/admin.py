from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname']


@admin.register(WorkerAddress)
class WorkerAddress(admin.ModelAdmin):
    list_display = ['id', 'worker']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname']


@admin.register(ClientAddress)
class ClientAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'client']


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['description', 'worker']


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'worker']
