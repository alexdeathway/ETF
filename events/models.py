from django.db import models
#from django
from django.contrib.auth import get_user_model

User=get_user_model()

class Event(models.Model):
    name=models.CharField(max_length=20)
    code=models.CharField(max_length=20,unique=True)
    description=models.TextField()
    cover=models.ImageField(upload_to="Event Cover", height_field=None, width_field=None, max_length=None)
    is_live=models.BooleanField(default=False)
    # available_seats=models.PositiveIntegerField()
    #this is to show if seats are available or not
    
    # @property
    # def 

    def __str__(self):
        return self.code

class TicketType(models.Model):    
    event=models.ForeignKey(Event, on_delete=models.CASCADE,related_name="TicketType_Event")
    price=models.PositiveIntegerField()
    type=models.CharField(max_length=50)
    limit=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type} type of ticket for {self.event}"


class Ticket(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Ticket_User")
    name=models.CharField( max_length=50)
    email=models.EmailField(max_length=20)
    type=models.ForeignKey(TicketType, on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    unique_id=None

    def __str__(self):
        return f"{self.owner} booked {self.type} ticket for {self.event}"