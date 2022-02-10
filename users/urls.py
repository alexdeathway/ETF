import profile
from django.urls import path 
from users.views import UserProfileView
app_name="users"

urlpatterns= [
    path("<slug:username>/",UserProfileView.as_view(),name="profile"),
]
