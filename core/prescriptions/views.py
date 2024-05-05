# views.py
from rest_framework import generics
from .models import Patient, Prescription
from .serializers import PatientSerializer, PrescriptionSerializer
from .permissions import IsDoctor

class PatientListAPIView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PrescriptionListAPIView(generics.ListAPIView):
    permission_classes = [IsDoctor]  # Ensure only doctors can access this view
    serializer_class = PrescriptionSerializer

    def get_queryset(self):
        national_code = self.request.query_params.get('national_code', None)
        mobile_number = self.request.query_params.get('mobile_number', None)
        if national_code:
            return Prescription.objects.filter(patient__national_code=national_code)
        elif mobile_number:
            return Prescription.objects.filter(patient__mobile_number=mobile_number)
        else:
            return Prescription.objects.all()
