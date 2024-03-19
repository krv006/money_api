from rest_framework import serializers
from .models import Category, Card, Consumption, Sub_category

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
    # 1 chisida nomini olish uchun ReadOnlyField ishlatildi
    # 2 chisida CharField status nomini olish uchun ishlatildi

    class Meta :
        model = Consumption
        fields = ['name', 'info', 'cost', 'sub_category_name', 'time', 'status_display', 'date']

