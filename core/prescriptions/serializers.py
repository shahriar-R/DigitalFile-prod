# serializers.py
from rest_framework import serializers
from .models import Patient, Prescription, NoteDetailEprsc, NoteDetailsReferral

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'national_code', 'mobile_number']

class PrescriptionSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Prescription
        fields = ['id', 'patient', 'doctor']  # Add other fields as needed

class NoteDetailEprscSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteDetailEprsc
        fields = '__all__'

class NoteDetailsReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteDetailsReferral
        fields = '__all__'
