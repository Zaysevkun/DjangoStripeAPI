from django.contrib import admin
from .models import Item, Order, Discount, Tax


class ItemAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.use = request.user
        obj.save()


admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Discount)
admin.site.register(Tax)
