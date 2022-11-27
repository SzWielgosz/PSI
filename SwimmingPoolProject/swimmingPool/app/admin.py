from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Worker)
admin.site.register(WorkerAddress)
admin.site.register(Client)
admin.site.register(ClientAdress)
admin.site.register(Shift)
admin.site.register(ShiftAssignment)
admin.site.register(Ticket)
admin.site.register(TicketAssignment)