from django.shortcuts import render,reverse
from django.contrib.auth import get_user_model
from django.views.generic import CreateView,TemplateView
from .forms import CustomUserCreationForm
from django.http import Http404

User=get_user_model()

class UserSignupView(CreateView):
    template_name="registration/signup.html"
    form_class=CustomUserCreationForm

    def get_success_url(self):
        return reverse("home")

class UserProfileView(TemplateView):
    template_name="users/profile.html"
    
    def get_context_data(self,**kwargs):
        username=self.kwargs.get('username',None)
        context=super(UserProfileView,self).get_context_data(**kwargs)
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404("User doesnt exists!")    
        
        context["profile"]=user
        return context