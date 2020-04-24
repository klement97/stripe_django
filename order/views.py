import json

import stripe
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from order.models import Product
from order.serializers import ProductSerializer

stripe.api_key = 'sk_test_s8jYTah3NcMusfHFnrGYbEzh00gblAakux'


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['GET'])
def create_payment_intent(request, product_id):
    product_instance = Product.objects.get(id=product_id)
    price_in_cents = int(product_instance.price * 100)
    intent = stripe.PaymentIntent.create(
        amount=price_in_cents,
        currency='usd',
        description='Test payment for Klement Omeri',
        metadata={'integration_check': 'accept_a_payment'},
    )
    content = json.dumps({'client_secret': intent['client_secret']})

    return HttpResponse(content, content_type='application/json', status=200)
