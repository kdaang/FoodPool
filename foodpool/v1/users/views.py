from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from foodpool.v1.users.serializers import AddressSerializer


class DeliveryAddressAPIView(APIView):
    serializer_class = AddressSerializer

    def post(self, request):
        address = request.data.get('address', {})

        # TODO: set user to request.user
        address['user'] = 1

        serializer = self.serializer_class(data=address)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

