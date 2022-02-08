from django.shortcuts import render
from django.urls import reverse
from events.forms import EventCreationForm ,TicketTypeCreationForm,TicketBookingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
                                    CreateView,
                                )  

class EventCreateView(LoginRequiredMixin,CreateView):

    template_name="events/event_create.html"
    form_class=EventCreationForm
    
    def get_success_url(self):
        reverse('home')

class TicketTypeCreateView(LoginRequiredMixin,CreateView):

    template_name="events/tickettype_create.html"
    form_class=TicketTypeCreationForm
    
    def get_success_url(self):
        reverse('home')


class TicketBookingView(LoginRequiredMixin,CreateView):

    template_name="events/ticket_booking.html"
    form_class=TicketBookingForm
    
    def get_success_url(self):
        reverse('home')        