from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname']

admin.site.register(WorkerAddress)
admin.site.register(Client)
admin.site.register(ClientAdress)
admin.site.register(Shift)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['zone', 'worker']
