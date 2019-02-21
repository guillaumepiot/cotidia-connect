from django import forms

from betterforms.forms import BetterForm, BetterModelForm

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


class BookingCancelForm(BetterModelForm):
    status_notes = forms.CharField(
        max_length=500,
        widget=forms.Textarea,
        label="Describe reasons for cancellation (optional)",
        required=False,
    )

    class Meta:
        model = Booking
        fields = ["status_notes"]
        fieldsets = (
            ("info", {"fields": ("status_notes",), "legend": "Cancel booking"}),
        )
