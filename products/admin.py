from django.contrib import admin
from .models import Product,Offer

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
  list_display= ('name','price','stock')

admin.site.register(Product,ProductAdmin)


class OfferProductAdmin(admin.ModelAdmin):
  list_display= ('code','discount')

admin.site.register(Offer,OfferProductAdmin)

