from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class DataForwardAPIView(APIView):
    def post(self, request):
        # Get data from the request
        data = request.data
        print(data)

        # Send the data to another server using HTTP POST request
        try:
            response = requests.post('https://ep-test.tamin.ir/api/SendEpresc', json=data)
            # Check if the request was successful
            if response.status_code == 200:
                return Response({'message': response}, status=200)
            else:
                print(response)
                return Response({'message': 'Failed to forward data'}, status=response.status_code)
        except Exception as e:
            return Response({'message': f'Error: {str(e)}'}, status=500)