from django.urls import path, include


app_name = "consult-admin"

urlpatterns = [
    path("service-type/", include("consult.urls.admin.servicetype")),
    path("customer/", include("consult.urls.admin.customer")),
    path("booking/", include("consult.urls.admin.booking")),
]
