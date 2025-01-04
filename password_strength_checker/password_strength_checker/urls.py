from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("strength_checker/", include("strength_checker.urls")),
    path("admin/", admin.site.urls),
]