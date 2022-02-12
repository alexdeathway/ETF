from django.shortcuts import render
from django.urls import reverse
from users.forms import CustomUserCreationForm
from django.views.generic import CreateView

class AdminSignupView(CreateView):
    template_name="registration/signup.html"
    form_class=CustomUserCreationForm

    def form_valid(self,form):
        user=form.save(commit=False)
        user.is_superuser=True
        user.save()
   
    def get_success_url(self):
        return reverse("home")

