from django.db import models

# Create your models here.
class restraunt(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

class account(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100 , default="abc@gmail.com")
    dob = models.DateField()
    joined_date = models.DateTimeField(auto_now_add=True)
    discount = models.FloatField(default=0.0)

class food(models.Model):
    name = models.CharField(max_length=50)
    restraunt = models.ForeignKey(restraunt,on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    added_date = models.DateTimeField(auto_now_add=True)

class order(models.Model):
    user = models.ForeignKey(account,on_delete=models.CASCADE)
    restraunt = models.ForeignKey(restraunt,on_delete=models.CASCADE)
    food = models.ForeignKey(food,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cost = models.FloatField(default=0.0)
    order_date = models.DateTimeField(auto_now_add=True)
