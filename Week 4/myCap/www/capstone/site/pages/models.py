from django.db import models

# Create your models here.

# class Menu_List(models.Model):
#     name = models.CharField(max_length=200)

class Menu_Item(models.Model):
    name = models.CharField(max_length=200) 
    description = models.TextField()
    price = models.FloatField()


    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=200) 
    description = models.TextField()
    price = models.FloatField()    
    img = models.CharField(max_length=300)

    def save(self,*args, **kwargs ):
        self.price = round(self.price , 2)
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.name