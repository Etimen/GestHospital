from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('medecin', 'Medecin'),
        ('infirmier', 'Infirmier'),
        ('patient', 'Patient'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='patient'
    )

    # Helper properties (very useful later)
    @property
    def is_doctor(self):
        return self.role == 'medecin'

    @property
    def is_patient(self):
        return self.role == 'patient'

    @property
    def is_nurse(self):
        return self.role == 'infirmier'

    def __str__(self):
        return f"{self.username} ({self.role})"


# -------------------------------
# Doctor Profile
# -------------------------------
class DoctorProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='doctor_profile'
    )
    specialty = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.user.username}"


# -------------------------------
# Patient Profile
# -------------------------------
class PatientProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.user.username