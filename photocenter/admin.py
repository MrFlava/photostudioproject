from django.contrib import admin

from .models import (PhotoCenter, PhotoOffice, PhotoStand, Order, Item, Provider,
                     ItemProvider, AdditionalService,  ItemOrder, AdditionalServicesOrder)

# Register your models here.


class PhotoCenterAdmin(admin.ModelAdmin):
    model = PhotoCenter


class PhotoOfficeAdmin(admin.ModelAdmin):
    model = PhotoOffice


class PhotoStandAdmin(admin.ModelAdmin):
    model = PhotoStand


class OrderAdmin(admin.ModelAdmin):
    model = Order


class ItemAdmin(admin.ModelAdmin):
    model = Item


class ProviderAdmin(admin.ModelAdmin):
    model = Provider


class ItemProviderAdmin(admin.ModelAdmin):
    model = ItemProvider


class AdditionalServiceAdmin(admin.ModelAdmin):
    model = AdditionalService


class ItemOrderAdmin(admin.ModelAdmin):
    model = ItemOrder


class AdditionalServicesOrderAdmin(admin.ModelAdmin):
    model = AdditionalServicesOrder


admin.site.register(AdditionalServicesOrder, AdditionalServicesOrderAdmin)
admin.site.register(AdditionalService, AdditionalServiceAdmin)
admin.site.register(ItemProvider, ItemProviderAdmin)
admin.site.register(PhotoCenter, PhotoCenterAdmin)
admin.site.register(PhotoOffice, PhotoOfficeAdmin)
admin.site.register(PhotoStand, PhotoStandAdmin)
admin.site.register(ItemOrder, ItemOrderAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)

