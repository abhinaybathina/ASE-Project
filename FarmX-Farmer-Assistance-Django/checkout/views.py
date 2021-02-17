from django.shortcuts import render, redirect
from .models import Addressandpayment
from cart.models import Cart, Order
from django.views.decorators.csrf import csrf_exempt
import stripe
from Farming_Assistance_Django import settings
stripe.api_key = settings.STRIPE_SECRET_KEY
key = settings.STRIPE_PUBLIC_KEY
# Create your views here.


def payform(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        return render(request, 'checkout/addrandpay.html', {'amount': amount, 'key': key})


@csrf_exempt
def checkout(request):
    if request.method == 'POST':
        token = request.POST.get("stripeToken")
        order = Order.objects.get(user=request.user, ordered=False)
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        city = request.POST['city']
        zipcode = request.POST['zipcode']
        user = request.user
        order_id = order.id
        amount = request.POST['amount']
        new_payment = Addressandpayment(user=user, order_id=order_id, name=name, email=email, address=address, phone=phone, city=city, zipcode=zipcode, amount=amount)
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency="inr",
                source=token,
                description="The product charged to the user"
            )
            new_payment.charge_id = charge.id
        except stripe.error.CardError as ce:
            return False, ce
        else:
            new_payment.save()
            return redirect('thankyou')


def thanks(request):
    order = Order.objects.get(user=request.user, ordered=False)
    order.ordered = True
    order.save()
    cartItems = Cart.objects.filter(user=request.user)
    for items in cartItems:
        items.purchased = True
        items.save()
    lis = []
    lis += order.orderitems.all()
    return render(request, 'checkout/thankyou.html', {"carts": lis, 'order': order})