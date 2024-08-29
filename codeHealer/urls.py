from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logistics/', include('logistics.urls')),
    path('cancer/', include('cancer_prediction.urls')),
    path('diabetes/', include('diabetes_prediction.urls')),
    path('heart/', include('heart_prediction.urls')),
]