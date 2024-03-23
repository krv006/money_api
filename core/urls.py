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

]

# statistika oy xafta yil oyliklar qilish rasxodlar 
# rasxodlar 