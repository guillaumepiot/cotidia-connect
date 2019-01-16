from django.urls import path

from consult.views.api.booking import BookingCalendarAPIView


urlpatterns = [
    path("calendar", BookingCalendarAPIView.as_view(), name="booking-calendar")
]
