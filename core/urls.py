from django.urls import path
from .views import *

urlpatterns = [

    path('categories/', CategoryListAPIView.as_view(), name='categories-list'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='categories-detail'),

    path('card/', CardListAPIView.as_view(), name='card-list'),
    path('card/<int:pk>/', CardRetrieveUpdateDestroyAPIView.as_view(), name='card-detail'),

    path('sub_category/', Sub_categoryListAPIView.as_view(), name='sub_category-list'),
    path('sub_category/<int:pk>/', Sub_categoryRetrieveUpdateDestroyAPIView.as_view(), name='sub_category-detail'),

    path('consumption/', ConsumptionListAPIView.as_view(), name='consumption-list'),
    path('consumption/<int:pk>/', ConsumptionRetrieveUpdateDestroyAPIView.as_view(), name='consumption-detail'),

    path('plastic_card/', Plastic_cardListAPIView.as_view(), name='plastic_card-list'),
    path('plastic_card/<int:pk>/', Plastic_cardRetrieveUpdateDestroyAPIView.as_view(), name='plastic_card-detail'),

    path('product/', ProductListAPIView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),

    path('debtors/', DebtorsListAPIView.as_view(), name='debtors-list'),
    path('debtors/<int:pk>/', DebtorsRetrieveUpdateDestroyAPIView.as_view(), name='debtors-detail'),
]

# statistika oy xafta yil oyliklar qilish rasxodlar 
# rasxodlar 