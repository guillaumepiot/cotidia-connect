from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from cotidia.account.views.admin import dashboard


urlpatterns = [
    path(
        "admin/account/",
        include("cotidia.account.urls.admin", namespace="account-admin"),
    ),
    path("admin/mail/", include("cotidia.mail.urls", namespace="mail-admin")),
    path(
        "admin/actionable/",
        include("cotidia.actionable.urls.admin", namespace="actionable-admin"),
    ),
    path("admin/team/", include("cotidia.team.urls.admin", namespace="team-admin")),
    path("admin/consult/", include("consult.urls.admin", namespace="consult-admin")),
    path(
        "admin/generic/", include("cotidia.admin.urls.admin", namespace="generic-admin")
    ),
    path("admin/", dashboard, name="dashboard"),
    path("api/generic/", include("cotidia.admin.urls.api", namespace="generic-api")),
    path("api/account/", include("cotidia.account.urls.api", namespace="account-api")),
    path("api/consult/", include("consult.urls.api", namespace="consult-api")),
    path("api/file/", include("cotidia.file.urls.api.file", namespace="file-api")),
    path(
        "api/actionable/",
        include("cotidia.actionable.urls.api", namespace="actionable-api"),
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns = [
        path(
            "media/<path>",
            serve,
            {"document_root": settings.MEDIA_ROOT, "show_indexes": True},
        )
    ] + urlpatterns
