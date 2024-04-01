from rest_framework import serializers
from .models import Category, Card, Consumption, Sub_category, Plastic_card, Product, Debtors, Workers, Camunalca, Dollars, Department, Employee

class Sub_categorySerializer(serializers.ModelSerializer):

    class Meta :
        model = Sub_category
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):

    sub_category = Sub_categorySerializer(many=True)
    
    class Meta :
        model = Category
        fields = ['name', 'info', 'sub_category']


class CardSerializer(serializers.ModelSerializer):

    class Meta :
        model = Card
        fields = ['plastic_name']


class ConsumptionSerializer(serializers.ModelSerializer):
    sub_category_name = serializers.ReadOnlyField(source='sub_category.name') 
    status_display = serializers.CharField(source='get_status_display') 
    # 1 chisida nomini olish uchun ReadOnlyField ishlatildi faqat oqish uchun
    # 2 chisida CharField status nomini olish uchun ishlatildi

    class Meta :
        model = Consumption
        fields = ['name', 'info', 'cost', 'sub_category_name', 'time', 'status_display', 'date']


class Plastic_cardSerializer(serializers.ModelSerializer):

    class Meta :
        model = Plastic_card
        fields = ['plastic_name', 'cost']

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta :
        model = Product
        fields = ['name', 'quantity', 'price', 'user']

class DebtorsSerializer(serializers.ModelSerializer):

    class Meta :
        model = Debtors
        fields = ['full_name', 'phone_numuber', 'product', 'date', 'price']


class WorkersSerializer(serializers.ModelSerializer):

    class Meta :
        model = Workers
        fields = ['workers_salary_month', 'workers_salary_weeks', 'workers_salary_days', 'workers_salary_oclocs']


class CamunalcaSerializer(serializers.ModelSerializer):

    class Meta :
        model = Camunalca
        fields = ['water', 'gas', 'electricity', 'wifi', 'lands' ]



class DollarsSerializer(serializers.ModelSerializer):

    class Meta :
        model = Dollars
        fields = ['dollar', 'dollar_course']


# class DepartmentSerializer(serializers.ModelSerializer):

#     class Meta :
#         model = Department
#         fields = ['name', 'is_active']

# class EmployeeSerializer(serializers.ModelSerializer):
#     department_name = serializers.ReadOnlyField(source='department.name') 
#     # department ni name ni olindi
#     class Meta :
#         model = Employee
#         fields = ['name', 'department_name']