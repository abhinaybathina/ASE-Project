from django.urls import path, include
from . import views

urlpatterns = [
    path('addrandpay/', views.payform, name='addrandpay'),
    path('checkout/', views.checkout, name='checkout'),
    path('thankyou/', views.thanks, name='thankyou'),
]