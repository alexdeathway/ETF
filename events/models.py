from pyexpat import model
from django.db import models
#from django

# Create your models here.

class Event(models.Model):
    name=models.CharField( max_length=20)
    description=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    ticket_type_choices=(
        ("Normal","Normal"),
        ("Standard","Standard"),
        ("VIP","VIP")
    )
    event=models.OneToOneField(Event, on_delete=models.CASCADE)
    price=models.PositiveIntegerField(max_length=6)
    ticket_type=model