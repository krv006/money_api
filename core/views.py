from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Category, Card, Sub_category, Consumption, Plastic_card, Product, Debtors, Workers, Dollars, Camunalca
from .models import  Department, Employee, ParentCategory
from .serializers import CategorySerializer, CardSerializer, Sub_categorySerializer, ConsumptionSerializer
from .serializers import Plastic_cardSerializer, ProductSerializer, DebtorsSerializer 
from .serializers import WorkersSerializer, DollarsSerializer, CamunalcaSerializer
from .serializers import DepartmentSerializer, EmployeeSerializer, ParentCategorySerializer

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .permissions import IsAdminOrReadOnly
from rest_framework.pagination import PageNumberPagination


class ParentCategoryListAPIView(generics.ListCreateAPIView):
    serializer_class = ParentCategorySerializer

    def get_queryset(self):
        queryset = ParentCategory.objects.all()
        parent_id = self.request.query_params.get('parent_id', None)

        if parent_id:
            queryset = queryset.filter(parent_id=parent_id)



class ParentCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializer


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


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
    pagination_class = CustomPageNumberPagination




class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CardListAPIView(ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class DepartmentListAPIView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer



class EmployeeListAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer




class Plastic_cardListAPIView(ListCreateAPIView):
    queryset = Plastic_card.objects.all()
    serializer_class = Plastic_cardSerializer

class Plastic_cardRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Plastic_card.objects.all()
    serializer_class = Plastic_cardSerializer


class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = CustomPageNumberPagination



class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )



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
    serializer_class = CamunalcaSerializer(queryset, many = True)

class CamunalcaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Camunalca.objects.all()
    serializer_class = CamunalcaSerializer
