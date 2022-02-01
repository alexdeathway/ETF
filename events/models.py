from django.db import models
#from django


class Event(models.Model):
    name=models.CharField( max_length=20)
    description=models.CharField(max_length=50)
    cover=models.ImageField(upload_to="Event Cover", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name

class TicketType(models.Model):    
    event=models.ForeignKey(Event, on_delete=models.CASCADE)
    price=models.PositiveIntegerField(max=600)
    type=models.CharField(max_length=50)
    limit=models.PositiveIntegerField(max=7000)

    def __str__(self):
        return f"{{self.type}} type of {{self.event}}"


class Ticket(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField(max_length=50)
    event=models.ForeignKey(Event, on_delete=models.CASCADE)
    type=models.ForeignKey(TicketType, on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()

    def __str__(self):
        return f"{{self.type}} type of {{self.event}}"