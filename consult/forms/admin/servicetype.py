from django import forms

from betterforms.forms import BetterModelForm

from consult.models import ServiceType


class ServiceTypeAddForm(BetterModelForm):
    class Meta:
        model = ServiceType
        fields = ["name"]
        fieldsets = (("info", {"fields": ("name",), "legend": "Service type details"}),)


class ServiceTypeUpdateForm(ServiceTypeAddForm):
    pass
