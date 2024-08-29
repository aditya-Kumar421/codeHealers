from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
import pickle
import os


model_path = os.path.join(os.path.dirname(__file__), 'models', 'model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

class PredictAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            age = float(request.data.get('Age'))
            estimated_salary = float(request.data.get('EstimatedSalary'))

            input_query = np.array([[age, estimated_salary]])

            result = model.predict(input_query)[0]

            return Response({'purchased': int(result)}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
