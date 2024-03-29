from django.db import models
from django.db.models import aggregates,Sum
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.core.validators import MaxValueValidator

User=get_user_model()

class Event(models.Model):
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=20,unique=True)
    description=models.TextField()
    cover=models.ImageField(upload_to="Event Cover", height_field=None, width_field=None, max_length=None)
    is_live=models.BooleanField(default=False)
    date=models.DateField(auto_now=False, auto_now_add=False)
    time=models.TimeField( auto_now=False, auto_now_add=False)
    address=models.CharField(max_length=50)
    location_latitude=models.FloatField()
    location_longitude=models.FloatField()

    def __str__(self):
        return self.code

class TicketType(models.Model):    
    event=models.ForeignKey(Event, on_delete=models.CASCADE,related_name="TicketType_Event")
    price=models.PositiveIntegerField()
    type=models.CharField(max_length=50)
    amount=models.PositiveIntegerField()
    slug=models.SlugField(blank=True,null=True)

    #This is to show no. of available seats     
    @property
    def available_ticket(self):
        booked_ticket=Ticket.objects.filter(type=self).aggregate(Sum('amount'))['amount__sum']
        if booked_ticket is not None:
            return self.amount - booked_ticket  
        return self.amount
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.event} "+self.type)

        super(TicketType, self).save(*args, **kwargs)

    
    def __str__(self):
        return f"{self.type} type of ticket for {self.event}"


class Ticket(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Ticket_User")
    email=models.EmailField(max_length=50)
    type=models.ForeignKey(TicketType, on_delete=models.CASCADE)
    event=models.ForeignKey(Event, on_delete=models.CASCADE,related_name="Ticket_Event")
    amount=models.PositiveIntegerField()
    unique_id=None

    def __str__(self):
        return f"{self.owner} booked {self.type} ticket for {self.event.name}"