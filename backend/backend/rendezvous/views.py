from rest_framework import generics, permissions
from .models import RendezVous
from .serializers import RendezVousSerializer


class RendezVousListCreateView(generics.ListCreateAPIView):
    serializer_class = RendezVousSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = RendezVous.objects.all()

        # Role-based filtering
        if user.role == 'medecin':
            queryset = queryset.filter(doctor=user)
        elif user.role == 'patient':
            queryset = queryset.filter(patient=user)

        # Query param filtering
        status = self.request.query_params.get('status')
        date = self.request.query_params.get('date')

        if status:
            queryset = queryset.filter(status=status)

        if date:
            queryset = queryset.filter(date__date=date)

        return queryset