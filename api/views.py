from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseNotFound
from .models import Item
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_stripe_payment_indent(request, item_id=None):
    publish_key = settings.STRIPE_PUBLISHABLE_KEY
    secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'GET':
        item = get_object_or_404(Item, pk=item_id)

        stripe.api_key = secret_key
        intent = stripe.PaymentIntent.create(
            amount=item.price,
            currency='usd',
            payment_method_types=['card'],

        )
        return JsonResponse({'client_secret': intent.client_secret})

    return HttpResponseNotFound()
