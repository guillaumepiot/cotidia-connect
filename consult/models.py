from django.db import models

from cotidia.core.models import BaseModel, BaseAddress


class Customer(BaseModel, BaseAddress):

    TITLE_CHOICES = (
        ("MR", "Mr"),
        ("MRS", "Mrs"),
        ("MISS", "Miss"),
        ("MS", "Ms"),
        ("MX", "Mx"),
    )

    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    dob = models.DateField()
    user = models.ForeignKey("account.User", null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ("first_name", "last_name")
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    class SearchProvider:
        dynamic_list_serializer = "consult.serializers.customer.CustomerAdminSerializer"

    def __str__(self):
        return "{} {} {}".format(self.title, self.first_name, self.last_name)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def marker_foreground_color(self):
        return "FFFFFF"

    @property
    def marker_background_color(self):
        return "ff8a25"


class Booking(BaseModel):
    datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=9, decimal_places=2)
    service_type = models.ForeignKey("consult.ServiceType", on_delete=models.PROTECT)
    first_visit = models.BooleanField(default=False)
    notes = models.TextField(max_length=500)
    member = models.ForeignKey("team.Member", on_delete=models.PROTECT)
    customer = models.ForeignKey("consult.Customer", on_delete=models.PROTECT)

    class Meta:
        ordering = ("-datetime",)
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    class SearchProvider:
        dynamic_list_serializer = "consult.serializers.booking.BookingAdminSerializer"

    def __str__(self):
        return "{} {} ({})".format(self.datetime, self.customer, self.service_type)

    @property
    def calendar_title(self):
        time_str = f"{self.datetime:%H:%M}"
        return "{} - {}".format(time_str, self.customer.name)

    @property
    def calendar_url(self):
        return self.get_admin_detail_url()

    @property
    def date(self):
        return self.datetime.date()


class ServiceType(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name = "Service type"
        verbose_name_plural = "Service types"

    class SearchProvider:
        dynamic_list_serializer = (
            "consult.serializers.servicetype.ServiceTypeAdminSerializer"
        )

    def __str__(self):
        return "{}".format(self.name)
