from rest_framework import serializers

from cotidia.admin.serializers import BaseDynamicListSerializer
from cotidia.team.serializers import MemberAdminSerializer

from consult.models import Booking
from consult.serializers.servicetype import ServiceTypeAdminSerializer
from consult.serializers.customer import CustomerAdminSerializer


class BookingAdminSerializer(BaseDynamicListSerializer):
    service_type = ServiceTypeAdminSerializer()
    member = MemberAdminSerializer()
    customer = CustomerAdminSerializer()

    class Meta:
        model = Booking
        exclude = ["id"]

    class SearchProvider:
        display_field = "name"
        filters = "__all__"
        default_columns = ["datetime", "time", "member", "customer", "service_type"]
        general_query_fields = [
            "member__first_name",
            "member__last_name",
            "customer__first_name",
            "customer__last_name" "service_type__name",
        ]

        toolbar_filters = ["datetime"]


class BookingCalendarSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="calendar_title")
    url = serializers.CharField(source="calendar_url")
    date = serializers.DateField()

    class Meta:
        model = Booking
        fields = ("title", "date", "service_type", "url")

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # ret["job_uuid"] = instance.callsheet.uuid
        # ret["day_reference"] = instance.day_reference
        # ret["day_reference_complete"] = instance.get_day_reference()
        # ret["status_verbal"] = instance.status_verbal()
        # ret["client"] = instance.callsheet.client.__str__()

        return ret
