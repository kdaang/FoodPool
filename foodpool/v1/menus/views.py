from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from foodpool.v1.menus.models import Restaurant
from foodpool.v1.menus.serializers import RestaurantSerializer


class RestaurantAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RestaurantSerializer

    def get(self, request):

        serializer = self.serializer_class(Restaurant.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class MenuAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = MenuSerializer
#
#     def get(self, request):
#         pass
