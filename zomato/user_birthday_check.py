from datetime import date
from celery import shared_task
from zomato.models import account

@shared_task
def check_birthday():
    today = date.today()
    users = account.objects.filter(dob_month=today.month,dob_day=today.day)
    for user in users:
        user.discount = 50
        user.save()