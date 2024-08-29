from django.urls import path
from .views import PredictCancerAPIView

urlpatterns = [
    path('predictCancer/', PredictCancerAPIView.as_view(), name='predictCancer'),
]
