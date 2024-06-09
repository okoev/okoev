from django.db import models
from django.contrib.auth.models import User
from datetime import date


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    image = models.ImageField()
    bio = models.TextField()
    date_of_birth = models.CharField

    def __str__(self):
        return self.user

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=50)
    license_number = models.SmallIntegerField()
    years_of_experience =models.IntegerField
    education = models.CharField(max_length=32)
    hospital = models.CharField(max_length=32)

    def __str__(self):
        return self.specialty


class MedicalRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    record_type = models.CharField(max_length=32)
    description = models.CharField(max_length=50)
    date = models.DateField

    def __str__(self):
        return self.record_type


class Appointment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor =models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField

    def __str__(self):
        return self.doctor


class Medication(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    dosage = models.PositiveIntegerField()
    schedule = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class FitnessProgram(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=35)

    def __str__(self):
        return self.user



