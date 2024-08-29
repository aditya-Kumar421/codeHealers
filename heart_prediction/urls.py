from django.urls import path
from .views import PredictHeartAPIView

urlpatterns = [
    path('predictHeart/', PredictHeartAPIView.as_view(), name='predictDia'),
]
