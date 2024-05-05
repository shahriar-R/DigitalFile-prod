from django.urls import path

from .views import PrescriptionCreateAPIView

app_name = 'prescription'



urlpatterns = [
    path('prescriptions/',PrescriptionCreateAPIView.as_view(),name="prescriptions"),
]


