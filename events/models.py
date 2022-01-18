from django.db import models
from django.

# Create your models here.

class Event(models.Model):
    name=models.CharField( max_length=20)
    description=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    event=models.OneToOneField(Event, on_delete=models.CASCADE)
    price=models.PositiveIntegerField(max_length=6)
    ticket_type=