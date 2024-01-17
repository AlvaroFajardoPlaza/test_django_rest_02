from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app02/", include("app02.urls")),
    path("crm/", include("crm.urls"))
]
