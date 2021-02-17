from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from cart.models import Order

# Create your models here.

User = get_user_model()


class Addressandpayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.IntegerField()
    amount = models.IntegerField(default=0)
    email = models.EmailField(default="")
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f'Order id {self.order_id} of {self.user.username} Payment Details and Billing Address'





