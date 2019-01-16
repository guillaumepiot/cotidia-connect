from django.urls import path, include


app_name = "consult-api"

urlpatterns = [path("booking/", include("consult.urls.api.booking"))]
