from cotidia.admin.serializers import BaseDynamicListSerializer
from consult.models import ServiceType


class ServiceTypeAdminSerializer(BaseDynamicListSerializer):
    class Meta:
        model = ServiceType
        exclude = ["id"]

    class SearchProvider:
        display_field = "name"
        filters = "__all__"
