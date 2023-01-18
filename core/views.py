from django.shortcuts import render
from django.views.generic import TemplateView
from events.models import Event
from setup.mixins import SetupCompletedRequiredMixin

class Home(SetupCompletedRequiredMixin,TemplateView):
    template_name="home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event"] =Event.objects.filter(is_live=True).first() 
        return context
    