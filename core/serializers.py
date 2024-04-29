from decimal import Decimal
import requests
from rest_framework import serializers
from .models import Category, Card, Consumption, Sub_category, Plastic_card, Product, Debtors, Workers, Camunalca, Dollars 
from .models import Department, Employee, ParentCategory


class ParentCategorySerializer(serializers.ModelSerializer):

    id_display = serializers.SerializerMethodField()

    def get_id_display(self, obj):
        return f"ID: {obj.id}"

    class Meta :
        model = ParentCategory
        fields = ['id', 'id_display', 'name']


class Sub_categorySerializer(serializers.ModelSerializer):

    class Meta :
        model = Sub_category
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):

    sub_category = Sub_categorySerializer(many=True)
    
    class Meta :
        model = Category
        fields = ['id', 'name', 'info', 'sub_category']


class CardSerializer(serializers.ModelSerializer):

    class Meta :
        model = Card
        fields = ['id', 'plastic_name']


class ConsumptionSerializer(serializers.ModelSerializer):
    sub_category_name = serializers.ReadOnlyField(source='sub_category.name') 
    status_display = serializers.CharField(source='get_status_display') 
    # 1 chisida nomini olish uchun ReadOnlyField ishlatildi faqat oqish uchun
    # 2 chisida CharField status nomini olish uchun ishlatildi

    class Meta :
        model = Consumption
        fields = ['id', 'name', 'info', 'cost', 'sub_category_name', 'time', 'status_display', 'date', 'types_camunalca']


class Plastic_cardSerializer(serializers.ModelSerializer):

    class Meta :
        model = Plastic_card
        fields = ['id', 'plastic_name', 'cost']

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    price_usd = serializers.SerializerMethodField()
    price_uzs = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity', 'price_usd', 'price_uzs', 'user']

    def get_price_usd(self, obj):
        amount = Decimal(obj.price)
        from_currency = 'USD'
        to_currency = 'UZS'  
        conversion_rate = self.get_conversion_rate(from_currency, to_currency)
        if conversion_rate is None:
            return None
        converted_amount = amount / Decimal(conversion_rate)
        return converted_amount

    def get_price_uzs(self, obj):
        return obj.price

    def get_conversion_rate(self, from_currency, to_currency):
        API_ENDPOINT = "https://v6.exchangerate-api.com/v6/0f84fd60fa278bb9b3c8e126/latest/{}".format(from_currency)
        response = requests.get(API_ENDPOINT)
        data = response.json()
        return Decimal(data['conversion_rates'].get(to_currency, 0))


class DebtorsSerializer(serializers.ModelSerializer):

    class Meta :
        model = Debtors
        fields = ['id', 'full_name', 'phone_numuber', 'product', 'date', 'price']


class WorkersSerializer(serializers.ModelSerializer):

    class Meta :
        model = Workers
        fields = ['id', 'workers_salary_month', 'workers_salary_weeks', 'workers_salary_days', 'workers_salary_oclocs']


class CamunalcaSerializer(serializers.ModelSerializer):

    class Meta :
        model = Camunalca
        fields = ['id', 'water', 'gas', 'electricity', 'wifi', 'lands' ]



class DollarsSerializer(serializers.ModelSerializer):

    class Meta :
        model = Dollars
        fields = ['id', 'dollar', 'dollar_course']


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta :
        model = Department
        fields = ['id', 'name', 'is_active']

class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.ReadOnlyField(source='department.name') 
    # department ni name ni olindi
    
    class Meta :
        model = Employee
        fields = ['id', 'name', 'department_name']


