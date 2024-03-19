from rest_framework import serializers
from .models import Category, Card, Consumption, Sub_category

class Sub_categorySerializer(serializers.ModelSerializer):

    class Meta :
        model = Sub_category
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    
    sub_category = serializers.PrimaryKeyRelatedField(many=True, queryset=Sub_category.objects.all())
    
    class Meta :
        model = Category
        fields = ['name', 'info', 'sub_category']


class CardSerializer(serializers.ModelSerializer):

    class Meta :
        model = Card
        fields = ['plastic_name']


class ConsumptionSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Consumption
        fields = ['name', 'info', 'cost', 'sub_category', 'time', 'status', 'date']

