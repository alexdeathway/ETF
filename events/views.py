from re import template
from django.forms import SlugField
from django.shortcuts import render
from django.urls import reverse
from events.forms import EventCreationForm ,TicketTypeCreationForm,TicketBookingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
                                ListView,    
                                CreateView,
                                DetailView,
                                )  

from events.models import Event

class EventListView(ListView):
    pass

class EventCreateView(LoginRequiredMixin,CreateView):

    template_name="events/event_create.html"
    form_class=EventCreationForm
    
    def get_success_url(self):
        reverse('home')

class EventDetailView(DetailView):
      template_name="events/event_detail.html"
      model=Event
      slug_url_kwarg="code"
      slug_field="code"

      def get_context_data(self,**kwargs):
        context=super(EventDetailView,self).get_context_data(**kwargs)
        tickets=self.get_object().TicketType_Event.all()              
        context["tickets"]=tickets
        return context


class TicketTypeCreateView(LoginRequiredMixin,CreateView):
    template_name="events/tickettype_create.html"
    form_class=TicketTypeCreationForm
    
    def get_success_url(self):
        reverse('home')


class TicketListView(ListView):
    #handled  by EventDetailView
    pass

class TicketBookingView(LoginRequiredMixin,CreateView):

    template_name="events/ticket_booking.html"
    form_class=TicketBookingForm
    
    def get_success_url(self):
        reverse('home')        