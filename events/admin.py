from multiprocessing import Event
from django.contrib import admin
from .models import Event,Ticket
# Register your models here.
admin.site.register(Event)
admin.site.register(Ticket)
