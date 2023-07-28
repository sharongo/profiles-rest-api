from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'is similiar to a tradition django view',
            'Gives you most control over the aplicatiopn logic',
            'It mapped manually to urls'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
        
        
