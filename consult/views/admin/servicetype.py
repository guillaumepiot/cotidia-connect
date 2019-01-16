import django_filters

from cotidia.admin.views import (
    AdminListView,
    AdminDetailView,
    AdminDeleteView,
    AdminCreateView,
    AdminUpdateView,
)

from consult.models import ServiceType
from consult.forms.admin.servicetype import ServiceTypeAddForm, ServiceTypeUpdateForm


class ServiceTypeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Name")

    class Meta:
        model = ServiceType
        fields = ["name"]


class ServiceTypeList(AdminListView):
    columns = (("Name", "name"),)
    model = ServiceType
    filterset = ServiceTypeFilter
    row_actions = ["create", "update", "view", "delete"]


class ServiceTypeDetail(AdminDetailView):
    model = ServiceType
    permission_required = "consult.change_servicetype"
    fieldsets = [
        {
            "legend": "Service Type Details",
            "fields": [[{"label": "Name", "field": "name"}]],
        }
    ]


class ServiceTypeCreate(AdminCreateView):
    model = ServiceType
    form_class = ServiceTypeAddForm
    permission_required = "consult.add_servicetype"


class ServiceTypeUpdate(AdminUpdateView):
    model = ServiceType
    form_class = ServiceTypeUpdateForm
    permission_required = "consult.change_servicetype"


class ServiceTypeDelete(AdminDeleteView):
    model = ServiceType
    permission_required = "app.delete_servicetype"
