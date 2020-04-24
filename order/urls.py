from django.urls import path

from order.views import create_payment_intent, ProductListAPIView

urlpatterns = [
    path('product/', ProductListAPIView.as_view(), name='product'),
    path('create/payment/intent/<int:product_id>/', create_payment_intent, name='create-payment-intent'),
]
