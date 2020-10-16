from django.contrib import admin
from django.urls import path, include
from api import views

app_name = 'api'


urlpatterns = [
    path('items/<int:item_id>/buy', views.ItemBuyView.as_view()),
    path('items/<int:item_id>/', views.ItemView.as_view()),
]
