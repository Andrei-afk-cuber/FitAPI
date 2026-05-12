from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class DietView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass
