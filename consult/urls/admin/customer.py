from django.urls import path

from cotidia.admin.views import DynamicListView
from cotidia.admin.views.generic import AdminGenericExportView

from consult.views.admin.customer import (
    CustomerCreate,
    CustomerDetail,
    CustomerUpdate,
    CustomerDelete,
)
from consult.serializers import CustomerAdminSerializer

urlpatterns = [
    path(
        "",
        DynamicListView.as_view(),
        {
            "model": "customer",
            "app_label": "consult",
            "serializer_class": CustomerAdminSerializer,
            # 'endpoint': reverse_lazy("callsheet-api:finance-main"),
            "template_type": "padded",
        },
        name="customer-list",
    ),
    path(
        "map",
        DynamicListView.as_view(),
        {
            "model": "customer",
            "app_label": "consult",
            "serializer_class": CustomerAdminSerializer,
            # 'endpoint': reverse_lazy("callsheet-api:finance-main"),
            "template_type": "padded",
        },
        name="customer-list-map",
    ),
    path("add", CustomerCreate.as_view(), name="customer-add"),
    path("<pk>", CustomerDetail.as_view(), name="customer-detail"),
    path("<pk>/update", CustomerUpdate.as_view(), name="customer-update"),
    path("<pk>/delete", CustomerDelete.as_view(), name="customer-delete"),
    path(
        "export/csv",
        AdminGenericExportView.as_view(),
        {
            "model": "customer",
            "app_label": "consult",
            "serializer_class": CustomerAdminSerializer,
            "format": "csv",
            "filename": "Customers",
            "permission_required": "consult.change_customer",
        },
        name="customer-export-csv",
    ),
    path(
        "export/pdf",
        AdminGenericExportView.as_view(),
        {
            "model": "customer",
            "app_label": "consult",
            "serializer_class": CustomerAdminSerializer,
            "format": "pdf",
            "filename": "Customers",
            "permission_required": "consult.change_customer",
        },
        name="customer-export-pdf",
    ),
]
