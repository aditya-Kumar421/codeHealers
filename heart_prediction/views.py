from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
import pickle
import os

model_path = os.path.join(os.path.dirname(__file__), 'models', 'heart_attack_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

class PredictHeartAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            age = int(request.data.get('age'))
            sex = int(request.data.get('sex'))
            cp = int(request.data.get('cp'))
            trtbps = int(request.data.get('trtbps'))
            chol = int(request.data.get('chol'))
            fbs = int(request.data.get('fbs'))
            restecg = int(request.data.get('restecg'))
            thalachh = int(request.data.get('thalachh'))
            exng = int(request.data.get('exng'))
            oldpeak = float(request.data.get('oldpeak'))
            slp = int(request.data.get('slp'))
            caa = int(request.data.get('caa'))
            thall = int(request.data.get('thall'))

            input_query = np.array([[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, 
                                     exng, oldpeak, slp, caa, thall]])

            result = model.predict(input_query)[0]

            if not int(result):
                response_message = {
                    'output': int(result),
                    'message': "Good news! Based on the prediction, you have a low risk of heart attack. However, we recommend regular check-ups for your peace of mind."
                }
            else:
                response_message = {
                    'output': int(result),
                    'message': "Please note, the prediction indicates a potential risk of heart attack. It's important to consult with a healthcare professional for a thorough evaluation."
                }

            return Response(response_message, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
