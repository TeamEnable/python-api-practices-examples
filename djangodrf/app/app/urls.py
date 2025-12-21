from django.contrib import admin
from django.urls import path

# We wire DRF views directly here.
# For v0.1, keep it minimal and explicit.
from api.views import PaymentsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/payments/", PaymentsView.as_view()),
]
