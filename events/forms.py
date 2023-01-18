from contextlib import nullcontext
import re
from django.forms import ModelForm,forms
from django.shortcuts import get_object_or_404
from events.models import Event ,TicketType ,Ticket
from django import forms

class EventCreationForm(ModelForm):
    class Meta:
        model=Event
        # verbose_name = 'Event'
        # verbose_name_plural = 'Events'
        
        label={
            "name":"Event name"
        }

        fields=[
            "name",
            "cover",
            "code",
            "description",
            "date",
            "time",
            "address",
            "location_latitude",
            "location_longitude",
        ]

        def clean_code(self):
            code= self.cleaned_data['code_name']
            if not re.match(r'^[0-9a-zA-Z]*$',code):
                    raise forms.ValidationError("Sorry , you can only have alphanumeric in code.") 
            return code

class TicketTypeCreationForm(ModelForm):
    class Meta:
        model=TicketType
        verbose_name = 'ticket type'
        verbose_name_plural = 'ticket types'

        fields=[
                "event",
                "price",
                "type",
                "limit",
            ]


class TicketBookingForm(ModelForm):

    

    def __init__(self,*args, **kwargs):
            """
            Here kwargs are passed to form from views so that ticket fields can be initialized 
            for ex ticket type,event and amount of ticket left in specific event type 
            """
            slug=kwargs.pop("ticket_type")
            ticket_type_queryset=TicketType.objects.filter(slug=slug)
            ticket_type=ticket_type_queryset.first()
            super(TicketBookingForm,self).__init__(*args,**kwargs)
            self.fields['amount']=forms.IntegerField(min_value=0,max_value=ticket_type.available_ticket)
            self.fields['type']=forms.ModelChoiceField(queryset=ticket_type_queryset,initial=ticket_type)
            event=Event.objects.filter(code=ticket_type.event.code)
            self.fields['event']=forms.ModelChoiceField(queryset=event,initial=event.first())
    
    class Meta:
        model=Ticket
        verbose_name = 'Event ticket type'
        verbose_name_plural = 'Event ticket types'

        fields=[
                "event",
                "type",
                "amount",
            ]        
        
        labels={
            "amount": "No of tickets:",
        }