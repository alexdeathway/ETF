from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.shortcuts import redirect

class SuperUserAccessMixin(LoginRequiredMixin,UserPassesTestMixin):
    """
    check is user is superuser.  
    """
    def test_func(self):
        return self.request.user.is_superuser
    


# class TicketA                 
