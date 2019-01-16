from cotidia.admin.views import (
    AdminDetailView,
    AdminDeleteView,
    AdminCreateView,
    AdminUpdateView,
)

from consult.models import Customer
from consult.forms.admin.customer import CustomerAddForm, CustomerUpdateForm


class CustomerDetail(AdminDetailView):
    model = Customer
    permission_required = "consult.change_customer"
    fieldsets = [
        {
            "legend": "Customer Details",
            "fields": [
                [],
                [{"label": "Address Line 1", "field": "address_line_1"}],
                [{"label": "Address Line 2", "field": "address_line_2"}],
                [{"label": "Address Line 3", "field": "address_line_3"}],
                [{"label": "Address City", "field": "address_city"}],
                [{"label": "Address State", "field": "address_state"}],
                [{"label": "Address Postcode", "field": "address_postcode"}],
                [{"label": "Address Country", "field": "address_country"}],
                [{"label": "Lat", "field": "lat"}],
                [{"label": "Lng", "field": "lng"}],
                [{"label": "Point", "field": "point"}],
                [{"label": "Title", "field": "title"}],
                [{"label": "First Name", "field": "first_name"}],
                [{"label": "Last Name", "field": "last_name"}],
                [{"label": "Dob", "field": "dob"}],
                [{"label": "User", "field": "user"}],
            ],
        }
    ]


class CustomerCreate(AdminCreateView):
    model = Customer
    form_class = CustomerAddForm
    permission_required = "consult.add_customer"


class CustomerUpdate(AdminUpdateView):
    model = Customer
    form_class = CustomerUpdateForm
    permission_required = "consult.change_customer"


class CustomerDelete(AdminDeleteView):
    model = Customer
    permission_required = "app.delete_customer"
