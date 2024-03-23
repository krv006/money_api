from django.contrib import admin
from .models import Category, Card, Consumption, Sub_category, Plastic_card, Product, Debtors

# Register your models here.

admin.site.register(Category)
admin.site.register(Card)
admin.site.register(Consumption)
admin.site.register(Sub_category)
admin.site.register(Plastic_card)
admin.site.register(Product)
admin.site.register(Debtors)