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
#from setup.mixins import SetupCompletedRequiredMixin

class EventListView(ListView):
    template_name="events/event_list.html"
    queryset=Event.objects.filter(is_live=True)

class EventCreateView(LoginRequiredMixin,CreateView):

    template_name="events/event_create.html"
    form_class=EventCreationForm
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return reverse('home')    
    
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

    def form_valid(self,form):
        form.save()

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return reverse('home')
    
   


class TicketListView(ListView):
    #handled  by EventDetailView
    pass

class TicketBookingView(LoginRequiredMixin,CreateView):

    template_name="events/ticket_booking.html"
    form_class=TicketBookingForm

    def form_valid(self,form):
        ticket = form.save(commit=False)
        ticket.owner=self.request.user
        ticket.save()

        return super(TicketBookingView,self).form_valid(form)
    
    def get_success_url(self):
        reverse('home')        