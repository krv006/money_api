from django.db import models
from django.db import models as m
from django.contrib.auth.models import User


# Create your models here.

class Sub_category(models.Model):
    name = models.CharField(max_length = 250)
    def __str__(self):
        return self.name 



class Consumption(models.Model):
    CONSUPTION_CHOISES_FIELD = [
        (1, 'not_gived'),
        (2, 'paid'),
        (3, 'not_paid'),
        (4, 'pending'),
    ]
    name = models.CharField(max_length = 250)
    info = models.TextField(null = True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField( auto_now_add = True )
    time = models.TimeField(auto_now_add = False, null=True)
    status = models.IntegerField(choices=CONSUPTION_CHOISES_FIELD, default=1)
    sub_category = models.ForeignKey(Sub_category,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length = 250)
    info = models.TextField()    
    sub_category = models.ManyToManyField(Sub_category)
    
    def __str__(self):
        return self.name



class Card(models.Model):
    plastic_name = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.plastic_name 


class Plastic_card(models.Model):
    cost = models.IntegerField()
    plastic_name = models.ForeignKey(Card,on_delete = models.CASCADE )
    
    def __int__(self):
        return self.cost


class Product(m.Model):
    name = m.CharField(max_length=250)
    quantity = m.PositiveSmallIntegerField()
    price = m.DecimalField(max_digits=11, decimal_places=3)
    user = m.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Debtors(m.Model):
    full_name = m.CharField(max_length=250)
    phone_numuber = m.CharField(max_length=250, blank = True)
    product = m.ManyToManyField(Product)
    date = m.DateField(auto_now_add=True)
    price = m.DecimalField(max_digits=11, decimal_places=3)

    def __str__(self):
        return self.full_name


class Dollars(m.Model):
    dollar = m.IntegerField()
    dollar_course = m.IntegerField()

    def __int__(self):
        return self.dollar
    

class Camunalca(m.Model):
    water = m.IntegerField()
    gas = m.IntegerField()
    electricity = m.IntegerField()
    wifi = m.IntegerField()
    lands = m.IntegerField()    # lands soliqlar
    
    def __int__(self):
        return self.water

class Workers(m.Model):
    workers_salary_month = m.IntegerField()
    workers_salary_weeks = m.IntegerField()
    workers_salary_days = m.IntegerField()
    workers_salary_oclocs = m.IntegerField()

    def __int__(self):
        return self.workers_salary_month


class Department(m.Model):
    name = m.CharField(max_length = 50)
    is_active = m.BooleanField(default = True)

class Employee(m.Model):
    name = m.CharField(max_length = 100)
    department = m.ForeignKey(Department, on_delete = models.CASCADE, limit_choices_to = { 'is_active' : True})