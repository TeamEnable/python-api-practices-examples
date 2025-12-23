from django.urls import path
from api.views import PaymentsView

urlpatterns = [
    path("payments/", PaymentsView.as_view()),
]
