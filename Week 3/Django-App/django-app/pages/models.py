from django.db import models

# Create your models here.

# class Menu_List(models.Model):
#     name = models.CharField(max_length=200)

class Menu_Item(models.Model):
    # menu_item = models.ForeignKey(Menu_List, on_delete=models.CASCADE)
    name = models.CharField(max_length=200) 
    description = models.CharField(max_length=300)
    price = models.FloatField()


    def __str__(self):
        return self.name

