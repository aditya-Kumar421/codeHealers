from django.urls import path
from .views import PredictDiabetesAPIView

urlpatterns = [
    path('predictDia/', PredictDiabetesAPIView.as_view(), name='predictDia'),
]
