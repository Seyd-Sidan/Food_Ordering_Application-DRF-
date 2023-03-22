from django.urls import path
from zomato import views

urlpatterns = [
    path('register/',views.register_user,name='registraton'),
    path('foods_avail/',views.foods_available,name='foods'),
    path('food_order/',views.order_food,name='foord_order'),
]