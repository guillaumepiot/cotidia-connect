from django.urls import path

from consult.views.admin.servicetype import (
    ServiceTypeList,
    ServiceTypeCreate,
    ServiceTypeDetail,
    ServiceTypeUpdate,
    ServiceTypeDelete,
)

urlpatterns = [
    path("", ServiceTypeList.as_view(), name="servicetype-list"),
    path("add", ServiceTypeCreate.as_view(), name="servicetype-add"),
    path("<pk>", ServiceTypeDetail.as_view(), name="servicetype-detail"),
    path("<pk>/update", ServiceTypeUpdate.as_view(), name="servicetype-update"),
    path("<pk>/delete", ServiceTypeDelete.as_view(), name="servicetype-delete"),
]
