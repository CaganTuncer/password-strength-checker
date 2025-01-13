from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path("strength_checker/", include("strength_checker.urls")),
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/strength_checker/")),
]