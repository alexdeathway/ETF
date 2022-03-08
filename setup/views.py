from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
from django.views.generic import CreateView,TemplateView
from setup.mixins import SuperUserSignUpAccessMixin
from events.views import EventCreateView

class AdminSignupView(SuperUserSignUpAccessMixin,CreateView):
    template_name="setup/admin_signup.html"
    form_class=CustomUserCreationForm

    def form_valid(self,form):
        user=form.save(commit=False)
        user.is_superuser=True
        user.save()
   
        return super(AdminSignupView,self).form_valid(form)


    def get_success_url(self):
        return reverse("setup:admin_event_create")


class AdminEventCreateView(TemplateView):
      template_name="setup/admin_create_event.html"
      
