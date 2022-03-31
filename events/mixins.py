from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth import get_user_model
from django.shortcuts import redirect

class SuperUserAccessMixin(AccessMixin):
    """
    check is user is superuser.  
    """

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:  
            return super().dispatch(request, *args, **kwargs)
        elif request.user.is_authenticated:#if user is authenticated but isn't superuser
              return  redirect('home')
        else:
            return redirect('login')     
