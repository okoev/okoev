from rest_framework import viewsets, permissions
from .models import User,Doctor, MedicalRecord, Appointment, Medication, FitnessProgram
from .serializers import *
from allauth.account.views import SignupView
from rest_framework.exceptions import PermissionDenied

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        user_profile = self.get_object()
        if user_profile.user == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("Вы не можете изменить профиль другого пользователя")

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class  MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset =  MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


class  AppointmentViewSet(viewsets.ModelViewSet):
    queryset =  Appointment.objects.all()
    serializer_class = AppointmentSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    queryset =  Medication.objects.all()
    serializer_class = MedicationSerializer

class FitnessProgramViewSet(viewsets.ModelViewSet):
    queryset = FitnessProgram.objects.all()
    serializer_class =FitnessProgramSerializer