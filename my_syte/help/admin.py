from django.contrib import admin
from .models import UserProfile, Doctor, MedicalRecord, Appointment, Medication, FitnessProgram

admin.site.register(UserProfile)
admin.site.register(Doctor)
admin.site.register(MedicalRecord)
admin.site.register(Appointment)
admin.site.register(Medication)
admin.site.register(FitnessProgram)
