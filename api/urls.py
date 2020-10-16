from django.contrib import admin
from django.urls import path, include
from api import views

app_name = 'api'


urlpatterns = [
    path('buy/<int:item_id>', views.get_stripe_payment_indent)
]
