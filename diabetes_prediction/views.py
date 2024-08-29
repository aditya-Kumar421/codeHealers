from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
import pickle
import os

model_path = os.path.join(os.path.dirname(__file__), 'models', 'diabetes_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

class PredictDiabetesAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            pregnancies = int(request.data.get('Pregnancies'))
            glucose = int(request.data.get('Glucose'))
            blood_pressure = int(request.data.get('BloodPressure'))
            skin_thickness = int(request.data.get('SkinThickness'))
            insulin = int(request.data.get('Insulin'))
            bmi = float(request.data.get('BMI'))
            diabetes_pedigree_function = float(request.data.get('DiabetesPedigreeFunction'))
            age = int(request.data.get('Age'))

            input_query = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, 
                                     bmi, diabetes_pedigree_function, age]])

            result = model.predict(input_query)[0]

            if not int(result):
                response_message = {
                    'output': int(result),
                    'message': "Good news! Based on the prediction, you have a low risk of diabetes. However, we recommend regular check-ups for your peace of mind."
                }
            else:
                response_message = {
                    'output': int(result),
                    'message': "Please note, the prediction indicates a potential risk of diabetes. It's important to consult with a healthcare professional for a thorough evaluation."
                }

            return Response(response_message, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
