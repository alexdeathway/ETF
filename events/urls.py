from django.urls import path
from django.urls import path
from events.views import (
                        EventListView,
                        EventCreateView,
                        TicketTypeCreateView,
                        TicketBookingView,
                    )       
app_name="events"

urlpatterns = [
    path("",EventListView.as_view(),name='eventlist'),
    path("create/",EventCreateView.as_view(),name='eventcreate'),
    path("ticket-type-create/",TicketTypeCreateView.as_view(),name='tickettypecreate'),
    path("ticket-booking/",TicketBookingView.as_view(),name='ticketbooking'),
]
