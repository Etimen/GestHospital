from django.urls import path
from .views import RendezVousListCreateView

urlpatterns = [
    path('', RendezVousListCreateView.as_view()),
]