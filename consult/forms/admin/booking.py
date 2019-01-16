from django import forms

from betterforms.forms import BetterModelForm

from consult.models import Booking


class BookingAddForm(BetterModelForm):
    class Meta:
        model = Booking
        fields = [
            "datetime",
            "cost",
            "service_type",
            "first_visit",
            "notes",
            "member",
            "customer",
        ]
        fieldsets = (
            (
                "info",
                {
                    "fields": (
                        "datetime",
                        "cost",
                        "service_type",
                        "first_visit",
                        "notes",
                        "member",
                        "customer",
                    ),
                    "legend": "Booking details",
                },
            ),
        )


class BookingUpdateForm(BookingAddForm):
    pass
