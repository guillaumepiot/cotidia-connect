from django.urls import reverse


def admin_menu(context):
    return [
        {
            "text": "Customers",
            "icon": "user-friends",
            "url": reverse("consult-admin:customer-list"),
            "permissions": ["consult.add_customer", "team.change_customer"],
        },
        {
            "text": "Bookings",
            "icon": "calendar",
            "url": reverse("consult-admin:booking-calendar"),
            "permissions": ["consult.add_booking", "team.change_booking"],
        },
        {
            "icon": "",
            "text": "Services",
            "description": "Manage services provided.",
            "align_right": True,
            "nav_items": [
                {
                    "text": "Service types",
                    "icon": "award",
                    "url": reverse("consult-admin:servicetype-list"),
                    "permissions": [
                        "consult.add_servicetype",
                        "team.change_servicetype",
                    ],
                }
            ],
        },
    ]
