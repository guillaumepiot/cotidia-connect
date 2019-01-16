from django.urls import path

from cotidia.admin.views import DynamicListView

from consult.views.admin.booking import (
    BookingCalendar,
    BookingCreate,
    BookingDetail,
    BookingUpdate,
    BookingDelete,
)
from consult.serializers import BookingAdminSerializer

urlpatterns = [
    path(
        "",
        DynamicListView.as_view(),
        {
            "model": "booking",
            "app_label": "consult",
            "serializer_class": BookingAdminSerializer,
            # 'endpoint': reverse_lazy("callsheet-api:finance-main"),
            "template_type": "padded",
        },
        name="booking-list",
    ),
    path("calendar/", BookingCalendar.as_view(), name="booking-calendar"),
    path("add", BookingCreate.as_view(), name="booking-add"),
    path("<pk>", BookingDetail.as_view(), name="booking-detail"),
    path("<pk>/update", BookingUpdate.as_view(), name="booking-update"),
    path("<pk>/delete", BookingDelete.as_view(), name="booking-delete"),
]
