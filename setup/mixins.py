from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from events.models import Event
from django.contrib.auth.mixins import AccessMixin
User=get_user_model()

class SetupCompletedRequiredMixin:
    """   
    check if  superuser exists with atleast one event.
    activated during completing or checking status of setup.
    """
    def dispatch(self, request, *args, **kwargs):
        superuser=User.objects.filter(is_superuser=True).exists()
        if superuser:
            return super().dispatch(request, *args, **kwargs)           
        else:
            return redirect("setup:admin_singup") 
            
class SuperUserSignUpAccessMixin:
    """
    Verify privilage to Access superuser creation via frontend
    
    valid cases 1: No Super User exist. 
                2: Super User is creating another super user.
    """
    def dispatch(self, request, *args, **kwargs):
        superusers_exists=User.objects.filter(is_superuser=True).exists()
        if (self.request.user.is_superuser) or ( not superusers_exists ):  
            return super().dispatch(request, *args, **kwargs)
        elif request.user.is_authenticated:
              return  redirect('home')
        else:
            return redirect('login')     