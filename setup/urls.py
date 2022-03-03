from django.urls import path
from setup.views import AdminSignupView,AdminEventCreateView

app_name="setup"

urlpatterns = [
    path("admin/",AdminSignupView.as_view(),name="admin_singup"),
    path("create/",AdminEventCreateView.as_view(),name="admin_event_create"),
]
