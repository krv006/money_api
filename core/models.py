from django.db import models

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
    sub_category = models.ForeignKey(Sub_category,on_delete = models.CASCADE)
    time = models.TimeField(auto_now_add = False, null=True)
    status = models.IntegerField(choices=CONSUPTION_CHOISES_FIELD, default=1)
    date = models.DateField( auto_now_add = True )
    def __str__(self):
        return self.name


class Card(models.Model):
    plastic_name = models.CharField(max_length = 250)
    
    
    def __str__(self):
        return self.plastic_name 



class Category(models.Model):
    name = models.CharField(max_length = 250)
    info = models.TextField()    
    sub_category = models.ManyToManyField(Sub_category)
    
    def __str__(self):
        return self.name
    


# class Plastic_card(models.Model):
#     cost = models.IntegerField
#     Plastic_nmae = models.ForeignKey(Card,on_delete = models.CASCADE )
    
#     def __str__(self):
#         return self.cost
    
    