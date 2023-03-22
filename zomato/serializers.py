from rest_framework import serializers, fields
from .models import restraunt,account,food,order


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model= food
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'
