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

    class Meta :
        model = Product
        fields = ['id', 'name', 'quantity', 'price', 'user']

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


