from rest_framework import serializers

from foodpool.v1.menus.models import Restaurant, RestaurantLocation


class RestaurantLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantLocation
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = '__all__'

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)

    def get_location(self, restaurant):
        return RestaurantLocationSerializer(RestaurantLocation.objects.filter(restaurant=restaurant), many=True).data

