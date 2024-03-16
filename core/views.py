from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Category, Card, Sub_category, Consumption
from .serializers import CategorySerializer, CardSerializer, Sub_categorySerializer, ConsumptionSerializer
# from .serializers import 

class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CardListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CardSerializer

class CardListAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CardSerializer



class Sub_categoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = Sub_categorySerializer

class Sub_categoryListAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = Sub_categorySerializer



class ConsumptionListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = ConsumptionSerializer

class ConsumptionListAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = ConsumptionSerializer
