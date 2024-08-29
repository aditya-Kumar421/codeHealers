from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
import pickle
import os

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'models', 'cancer_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

class PredictCancerAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # diagnosis = int(request.data.get('diagnosis'))
            radius_mean = float(request.data.get('radius_mean'))
            texture_mean = float(request.data.get('texture_mean'))
            perimeter_mean = float(request.data.get('perimeter_mean'))
            area_mean = float(request.data.get('area_mean'))
            smoothness_mean = float(request.data.get('smoothness_mean'))
            compactness_mean = float(request.data.get('compactness_mean'))
            concavity_mean = float(request.data.get('concavity_mean'))
            concave_points_mean = float(request.data.get('concave points_mean'))
            symmetry_mean = float(request.data.get('symmetry_mean'))
            fractal_dimension_mean = float(request.data.get('fractal_dimension_mean'))
            radius_se = float(request.data.get('radius_se'))
            texture_se = float(request.data.get('texture_se'))
            perimeter_se = float(request.data.get('perimeter_se'))
            area_se = float(request.data.get('area_se'))
            smoothness_se = float(request.data.get('smoothness_se'))
            compactness_se = float(request.data.get('compactness_se'))
            concavity_se = float(request.data.get('concavity_se'))
            concave_points_se = float(request.data.get('concave points_se'))
            symmetry_se = float(request.data.get('symmetry_se'))
            fractal_dimension_se = float(request.data.get('fractal_dimension_se'))
            radius_worst = float(request.data.get('radius_worst'))
            texture_worst = float(request.data.get('texture_worst'))
            perimeter_worst = float(request.data.get('perimeter_worst'))
            area_worst = float(request.data.get('area_worst'))
            smoothness_worst = float(request.data.get('smoothness_worst'))
            compactness_worst = float(request.data.get('compactness_worst'))
            concavity_worst = float(request.data.get('concavity_worst'))
            concave_points_worst = float(request.data.get('concave points_worst'))
            symmetry_worst = float(request.data.get('symmetry_worst'))
            fractal_dimension_worst = float(request.data.get('fractal_dimension_worst'))
#diagnosis,
            input_query = np.array([[ radius_mean, texture_mean, perimeter_mean, area_mean, 
                                     smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, 
                                     symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, 
                                     area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, 
                                     symmetry_se, fractal_dimension_se, radius_worst, texture_worst, 
                                     perimeter_worst, area_worst, smoothness_worst, compactness_worst, 
                                     concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])

            result = model.predict(input_query)[0]

            return Response({'output': int(result)}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
