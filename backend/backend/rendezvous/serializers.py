from rest_framework import serializers
from .models import RendezVous


class RendezVousSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.username', read_only=True)
    doctor_name = serializers.CharField(source='doctor.username', read_only=True)

    class Meta:
        model = RendezVous
        fields = [
            'id',
            'patient',
            'doctor',
            'patient_name',
            'doctor_name',
            'date',
            'status',
            'reason',
            'created_at',
        ]