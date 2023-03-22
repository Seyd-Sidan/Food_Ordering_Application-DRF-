from django.shortcuts import render
from .models import account,food
from  rest_framework.decorators import api_view
from .serializers import AccountSerializer, FoodSerializer, OrderSerializer
from rest_framework.response import Response
import json
# Create your views here.


@api_view(['POST'])
def register_user(request):
    user_serializer = AccountSerializer(data=request.data)
    if user_serializer.is_valid():
        user_serializer.save()
        return Response("User Registration Successfull")
    else:
        return Response("User Registration Failed!!")


@api_view(['POST'])
def foods_available(request):
    res_id = request.data['restraunt_id']
    foods = food.objects.filter(restraunt=res_id)
    food_serializer = FoodSerializer(foods,many=True)
    return Response(food_serializer.data)

@api_view(['POST'])
def order_food(request):
    food_det = request.data
    user_det = account.objects.get(id=food_det['user'])
    food_item = food.objects.get(restraunt=food_det['restraunt'],id=food_det['food'])
    price = food_item.price
    if user_det.discount != 0:
        discount = user_det.discount
        cost = (price * food_det['quantity']) - discount
        food_det['cost'] = cost
    else:
        cost = (price * food_det['quantity'])
        food_det['cost'] = cost

    order_serializer = OrderSerializer(data=food_det)
    if order_serializer.is_valid():
        order_serializer.save()
        return Response("Order Successfull")
    else:
        print(order_serializer.errors)
        return Response("Order Failed!!!!")


