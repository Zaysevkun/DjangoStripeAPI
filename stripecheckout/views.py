import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import DetailView

from .models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemBuyView(DetailView):
    model = Order
    pk_url_kwarg = 'item_id'

    def get(self, request, *args, **kwargs):
        order = self.get_object()
        intent = self.get_intent(order)
        return JsonResponse({'client_secret': intent.client_secret})

    @staticmethod
    def get_intent(item):
        for item in Order.items.all():
            total_price = total_price + item.price

        # for discount in Order.discounts.all():

        return stripe.PaymentIntent.create(
            amount=total_price,
            currency='usd',
            payment_method_types=['card'],
            metadata={'integration_check': 'accept_a_payment'},
        )


class ItemView(DetailView):
    model = Order
    pk_url_kwarg = 'item_id'
    context_object_name = 'order'
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['client_secret'] = Book.objects.all()
    #     return context

