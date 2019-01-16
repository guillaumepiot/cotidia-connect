from django import forms

from betterforms.forms import BetterModelForm

from consult.models import Customer


class CustomerAddForm(BetterModelForm):
    class Meta:
        model = Customer
        fields = [
            "address_line_1",
            "address_line_2",
            "address_line_3",
            "address_city",
            "address_state",
            "address_postcode",
            "address_country",
            "lat",
            "lng",
            "title",
            "first_name",
            "last_name",
            "email",
            "dob",
            "user",
        ]
        fieldsets = (
            (
                "info",
                {
                    "fields": (
                        "address_line_1",
                        "address_line_2",
                        "address_line_3",
                        "address_city",
                        "address_state",
                        "address_postcode",
                        "address_country",
                        "lat",
                        "lng",
                        "title",
                        "first_name",
                        "last_name",
                        "email",
                        "dob",
                        "user",
                    ),
                    "legend": "Customer details",
                },
            ),
        )


class CustomerUpdateForm(CustomerAddForm):
    pass
