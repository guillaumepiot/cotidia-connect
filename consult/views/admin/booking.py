from cotidia.admin.views import (
    AdminListView,
    AdminDetailView,
    AdminDeleteView,
    AdminCreateView,
    AdminUpdateView,
)

from consult.models import Booking
from consult.forms.admin.booking import BookingAddForm, BookingUpdateForm


class BookingCalendar(AdminListView):
    model = Booking
    permission_required = "consult.change_booking"
    template_name = "admin/consult/booking/calendar.html"


class BookingDetail(AdminDetailView):
    model = Booking
    permission_required = "consult.change_booking"
    fieldsets = [
        {
            "legend": "Booking Details",
            "fields": [
                [],
                [{"label": "Date & Time", "field": "datetime"}],
                [{"label": "Cost", "field": "cost"}],
                [{"label": "Service Type", "field": "service_type"}],
                [{"label": "First Visit", "field": "first_visit"}],
                [{"label": "Notes", "field": "notes"}],
                [{"label": "Member", "field": "member"}],
                [{"label": "Customer", "field": "customer"}],
            ],
        }
    ]


class BookingCreate(AdminCreateView):
    model = Booking
    form_class = BookingAddForm
    permission_required = "consult.add_booking"


class BookingUpdate(AdminUpdateView):
    model = Booking
    form_class = BookingUpdateForm
    permission_required = "consult.change_booking"


class BookingDelete(AdminDeleteView):
    model = Booking
    permission_required = "app.delete_booking"
