import re
from django.forms import ModelForm,forms
from events.models import Event ,TicketType ,Ticket

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
            "code",
            "description",
            "cover",
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
    
    class Meta:
        model=Ticket
        verbose_name = 'event ticket type'
        verbose_name_plural = 'event ticket types'

        labels={
            "name": "Ticket type",
        }

        fields=[
                "name",
                "email",
                "type",
                "amount",
            ]        