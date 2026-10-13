from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.TextField()

# M : N 관계 (Doctor와 Patient의 관계) => Reservation 모델을 통해 관리
# through = "Reservation"
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserver_at = models.DateTimeField(auto_now_add=True)
