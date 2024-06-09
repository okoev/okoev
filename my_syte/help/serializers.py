from rest_framework import serializers
from .models import User,Doctor, MedicalRecord, Appointment, Medication, FitnessProgram

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'all'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = 'all'

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = 'all'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = 'all'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = 'all'

class FitnessProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessProgram
        fields = 'all'

