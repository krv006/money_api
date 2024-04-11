from django.urls import path
from .views import ParentCategoryListAPIView, ParentCategoryRetrieveUpdateDestroyAPIView,DepartmentListAPIView, DepartmentRetrieveUpdateDestroyAPIView
from .views import EmployeeListAPIView, EmployeeRetrieveUpdateDestroyAPIView, CardListAPIView, CardRetrieveUpdateDestroyAPIView, Sub_categoryListAPIView, Sub_categoryRetrieveUpdateDestroyAPIView
from .views import CategoryListAPIView, CategoryRetrieveUpdateDestroyAPIView, ConsumptionListAPIView, ConsumptionRetrieveUpdateDestroyAPIView
from .views import Plastic_cardListAPIView, Plastic_cardRetrieveUpdateDestroyAPIView, ProductListAPIView, ProductRetrieveUpdateDestroyAPIView, DebtorsListAPIView, DebtorsRetrieveUpdateDestroyAPIView
from .views import WorkersListAPIView, WorkersRetrieveUpdateDestroyAPIView, DollarsListAPIView, DollarsRetrieveUpdateDestroyAPIView
from .views import CamunalcaListAPIView, CamunalcaRetrieveUpdateDestroyAPIView

urlpatterns = [

    path('parentcategory/', ParentCategoryListAPIView.as_view(), name='category-list-create'),
    path('parentcategory/<int:pk>/', ParentCategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),

    path('department/', DepartmentListAPIView.as_view(), name='department-list'),
    path('department/<int:pk>/', DepartmentRetrieveUpdateDestroyAPIView.as_view(), name='department-detail'),

    path('employee/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('employee/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-detail'),

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
    # path('productdelete/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    # delete ni korib chiqish kerak ertaga shamshod bilan 

    path('debtors/', DebtorsListAPIView.as_view(), name='debtors-list'),
    path('debtors/<int:pk>/', DebtorsRetrieveUpdateDestroyAPIView.as_view(), name='debtors-detail'),

    path('workers/', WorkersListAPIView.as_view(), name='workers-list'),
    path('workers/<int:pk>/', WorkersRetrieveUpdateDestroyAPIView.as_view(), name='workers-detail'),

    path('dollars/', DollarsListAPIView.as_view(), name='dollars-list'),
    path('dollars/<int:pk>/', DollarsRetrieveUpdateDestroyAPIView.as_view(), name='dollars-detail'),

    path('camunalca/', CamunalcaListAPIView.as_view(), name='camunalca-list'),
    path('camunalca/<int:pk>/', CamunalcaRetrieveUpdateDestroyAPIView.as_view(), name='camunalca-detail'),
]

# statistika oy xafta yil oyliklar qilish rasxodlar 
# rasxodlar 