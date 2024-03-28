from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Category, Card, Sub_category, Consumption, Plastic_card, Product, Debtors, Workers, Dollars, Camunalca
from .serializers import CategorySerializer, CardSerializer, Sub_categorySerializer, ConsumptionSerializer
from .serializers import Plastic_cardSerializer, ProductSerializer, DebtorsSerializer 
from .serializers import WorkersSerializer, DollarsSerializer, CamunalcaSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .permissions import IsAdminOrReadOnly

class Sub_categoryListAPIView(ListCreateAPIView):
    queryset = Sub_category.objects.all()
    serializer_class = Sub_categorySerializer

class Sub_categoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sub_category.objects.all()
    serializer_class = Sub_categorySerializer


class ConsumptionListAPIView(ListCreateAPIView):
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer

class ConsumptionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer
    
class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CardListAPIView(ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer



class Plastic_cardListAPIView(ListCreateAPIView):
    queryset = Plastic_card.objects.all()
    serializer_class = Plastic_cardSerializer

class Plastic_cardRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Plastic_card.objects.all()
    serializer_class = Plastic_cardSerializer


class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DebtorsListAPIView(ListCreateAPIView):
    queryset = Debtors.objects.all()
    serializer_class = DebtorsSerializer

class DebtorsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Debtors.objects.all()
    serializer_class = DebtorsSerializer

class WorkersListAPIView(ListCreateAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer

class WorkersRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer


class DollarsListAPIView(ListCreateAPIView):
    queryset = Dollars.objects.all()
    serializer_class = DollarsSerializer

class DollarsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Dollars.objects.all()
    serializer_class = DollarsSerializer

class CamunalcaListAPIView(ListCreateAPIView):
    queryset = Camunalca.objects.all()
    serializer_class = CamunalcaSerializer

class CamunalcaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Camunalca.objects.all()
    serializer_class = CamunalcaSerializer