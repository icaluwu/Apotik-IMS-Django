from django.contrib import admin
from django.urls import path, include
from inventory import views as inventory_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("inventory.urls")),
    path("reports/", include("reports.urls")),
    path("login/", inventory_views.login_view, name="login"),
    path("logout/", inventory_views.logout_view, name="logout"),
]
