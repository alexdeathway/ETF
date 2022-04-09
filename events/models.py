from django.db import models
from django.db.models import aggregates,Sum
from django.contrib.auth import get_user_model

User=get_user_model()

class Event(models.Model):
    name=models.CharField(max_length=20)
    code=models.CharField(max_length=20,unique=True)
    description=models.TextField()
    cover=models.ImageField(upload_to="Event Cover", height_field=None, width_field=None, max_length=None)
    is_live=models.BooleanField(default=False)
   
            

    def __str__(self):
        return self.code

class TicketType(models.Model):    
    event=models.ForeignKey(Event, on_delete=models.CASCADE,related_name="TicketType_Event")
    price=models.PositiveIntegerField()
    type=models.CharField(max_length=50)
    limit=models.PositiveIntegerField()

    #this is to show  no. of available seats     
    @property
    def available_ticket(self):
        booked_ticket=Ticket.objects.filter(type=self).aggregate(Sum('amount'))['amount__sum']
        if booked_ticket is not None:
            return self.limit - booked_ticket  
        return self.limit
    
    def __str__(self):
        return f"{self.type} type of ticket for {self.event}"


class Ticket(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Ticket_User")
    name=models.CharField( max_length=50)
    email=models.EmailField(max_length=50)
    type=models.ForeignKey(TicketType, on_delete=models.CASCADE)
    event=models.ForeignKey(Event, on_delete=models.CASCADE,related_name="Ticket_Event")
    amount=models.PositiveIntegerField()
    unique_id=None

    def __str__(self):
        return f"{self.owner} booked {self.type} ticket for {self.event.name}"