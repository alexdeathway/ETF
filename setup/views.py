from django.shortcuts import render
from django.urls import reverse
from users.forms import CustomUserCreationForm
from django.views.generic import CreateView,TemplateView
from django.contrib.auth import get_user_model

User=get_user_model()

class AdminSignupView(CreateView):
    template_name="setup/admin_signup.html"
    form_class=CustomUserCreationForm

    def form_valid(self,form):
        user=form.save(commit=False)
        user.is_superuser=True
        user.save()
   
        return super(AdminSignupView,self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        superusers_exists=User.objects.filter(is_superuser=True).exist
        if (self.request.user.is_superuser) or ( not superusers_exists ):  
            return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("setup:admin_event_create")


class AdminEventCreateView(TemplateView):
      template_name="setup/admin_create_event.html"
      
