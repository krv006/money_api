from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Category, Card, Sub_category, Consumption
from .serializers import CategorySerializer, CardSerializer, Sub_categorySerializer, ConsumptionSerializer
# from .serializers import 



class Sub_categoryListAPIView(ListCreateAPIView):
    queryset = Sub_category.objects.all()
    serializer_class = Sub_categorySerializer

class Sub_categoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sub_category.objects.all()
    serializer_class = Sub_categorySerializer



class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # serializer_class = Sub_categoryListAPIView
    
    # def get_queryset(self):
    #     queryset = Category.objects.all()
    #     category_name = self.request.query_params.get("category_name", None)

    #     if category_name:
    #         queryset = queryset.filter(category_name = category_name)
    #     return queryset

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CardListAPIView(ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer





class ConsumptionListAPIView(ListCreateAPIView):
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer

class ConsumptionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer
