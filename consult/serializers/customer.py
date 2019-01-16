from rest_framework import serializers

from cotidia.admin.serializers import BaseDynamicListSerializer
from consult.models import Customer


class CustomerAdminSerializer(BaseDynamicListSerializer):
    name = serializers.CharField()
    address = serializers.CharField(source="address_to_string")
    marker_foreground_color = serializers.CharField()
    marker_background_color = serializers.CharField()

    class Meta:
        model = Customer
        exclude = ["id", "point", "user"]

    class SearchProvider:
        display_field = "name"
        filters = "__all__"
        default_columns = ["name", "email", "dob", "address"]
        general_query_fields = [
            "first_name",
            "last_name",
            "email",
            "address_line_1",
            # "address_line_2",
            # "address_line_3",
            "address_city",
            # "address_state",
            # "address_country",
            "address_postcode",
        ]

        field_representation = {
            "name": {"ordering_fields": ["first_name", "last_name"]}
        }

        # toolbar_filters = ["date"]
        sidebar_filters = ["name", "address_city", "address_postcode", "dob"]

        allowed_results_modes = ["table", "list", "map"]
        default_results_mode = "list"
        list_fields = {
            "left": {"top": "name", "bottom": "address"},
            "right": {"top": "dob", "bottom": ""},
        }
        default_per_page = 10000  # Show "most" results on the map
        map_configuration = {
            "defaultCoords": [
                {"lat": 57.3165865, "lng": -13.4594233},
                {"lat": 50.3232307, "lng": 5.0124407},
            ],
            "marker": {
                "labelField": "name",
                "foregroundField": "marker_foreground_color",
                "backgroundField": "marker_background_color",
            },
        }

        global_actions = [
            {
                "action": "export-as-csv",
                "label": "CSV",
                "icon": "file-excel",
                "classes": "btn--default",
                "function_template": "admin/consult/customer/js/export_csv.js",
            },
            {
                "action": "export-as-pdf",
                "label": "PDF",
                "icon": "file-pdf",
                "classes": "btn--default",
                "function_template": "admin/consult/customer/js/export_pdf.js",
            },
        ]
