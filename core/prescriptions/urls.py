from django.urls import path

from .views import PatientListAPIView,

app_name = 'prescription'



urlpatterns = [
    path('patientlist/',PatientListAPIView.as_view(),name="patientlist"),
    path('prescriptionlist/',PrescriptionListAPIView.as_view(),name="prescriptionlist"),
]


