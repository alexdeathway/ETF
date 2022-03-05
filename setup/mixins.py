from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from events.models import Event
User=get_user_model()

class SetupCompletedRequiredMixin:
    """   
    check if  superuser exists with atleast one event.
    """
    def dispatch(self, request, *args, **kwargs):
        superuser=User.objects.filter(is_superuser=True).exists()
        if superuser:
            return super().dispatch(request, *args, **kwargs)           
        else:
            return redirect("setup:admin_singup") 
            
            
# class SuperUserExistMixin:
     
#     def dispatch(self, request, *args, **kwargs):
#         superuser=User.objects.filter(is_superuser=True).exists()
#         if superuser: 
#             return super().dispatch(request, *args, **kwargs)
#         else:
#             return redirect("setup:admin_singup")