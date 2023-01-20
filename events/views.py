import folium
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

from events.models import Event,TicketType
from events.mixins import SuperUserAccessMixin

class EventListView(ListView):
    template_name="events/event_list.html"
    model=Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] =Event.objects.filter(is_live=True)
        return context
    

class EventCreateView(SuperUserAccessMixin,CreateView):

    template_name="events/event_create.html"
    form_class=EventCreationForm
    
    def get_success_url(self):
        return reverse('home')

class EventDetailView(DetailView):
      template_name="events/event_detail.html"
      model=Event
      slug_url_kwarg="code"
      slug_field="code"
      context_object_name="event"

      def get_context_data(self,**kwargs):
        context=super(EventDetailView,self).get_context_data(**kwargs)
        tickets=self.get_object().TicketType_Event.all()
        tickets=TicketType.objects.filter(event=self.get_object())
        event_coords=(self.get_object().location_latitude,self.get_object().location_longitude)
        event_map = folium.Map(location=event_coords, zoom_start=9)   
        folium.Marker(event_coords,popup=self.get_object().address).add_to(event_map)        
        context["tickets"]=tickets
        context["map"]=event_map._repr_html_()
        return context


class TicketTypeCreateView(SuperUserAccessMixin,CreateView):
    template_name="events/tickettype_create.html"
    form_class=TicketTypeCreationForm

    def form_valid(self,form):
        form.save() 
        return super(TicketTypeCreateView,self).form_valid(form)
    
    def get_success_url(self):
        return reverse('events:eventlist')

class TicketListView(ListView):
    #handled  by EventDetailView
    pass

class TicketBookingView(LoginRequiredMixin,CreateView):
    
    """
    Using TicketType slug to access the ticket type.
    """

    template_name="events/ticket_booking.html"
    form_class=TicketBookingForm

    def get_form_kwargs(self,**kwargs):
        kwargs=super(TicketBookingView,self).get_form_kwargs(**kwargs)
        kwargs.update({
            #for initial value in form
            "ticket_type":self.kwargs.get('ticket_slug')
        })
        return kwargs

    def form_valid(self,form):
        ticket = form.save(commit=False)
        ticket.owner=self.request.user
        ticket.email=self.request.user.email
        ticket.save()
        return super(TicketBookingView,self).form_valid(form)
        
    
    def get_success_url(self):
        return reverse('home')  

    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)
          