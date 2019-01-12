from django.db import models

from cotidia.core.models import BaseModel, BaseAddress

TITLE_CHOICES = (
    ("MR", "Mr"),
    ("MRS", "Mrs"),
    ("MISS", "Miss"),
    ("MS", "Ms"),
    ("MX", "Mx"),
)


class Customer(BaseModel, BaseAddress):
    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    user = models.ForeignKey("account.User", null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ("first_name", "last_name")
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Booking(BaseModel):
    date = models.DateField()
    time = models.TimeField()
    cost = models.DecimalField(max_digits=9, decimal_places=2)
    service_type = models.ForeignKey("consult.ServiceType", on_delete=models.PROTECT)
    first_visit = models.BooleanField(default=False)
    notes = models.TextField(max_length=500)
    member = models.ForeignKey("team.Member", on_delete=models.PROTECT)
    customer = models.ForeignKey("consult.Customer", on_delete=models.PROTECT)

    class Meta:
        ordering = ("-date",)
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"


class ServiceType(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name = "Service type"
        verbose_name_plural = "Service types"
