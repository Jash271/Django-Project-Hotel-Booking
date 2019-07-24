from django.db import models

# Create your models here.
class rooms(models.Model):
    Roomtypecode=models.CharField(max_length=100)
    Roomcode=models.IntegerField()
    typename=models.TextField(max_length=100)
    capacity=models.TextField(max_length=100)
    img=models.ImageField( upload_to = 'pics')
    Availible=models.BooleanField(default=True)


class guest(models.Model):
    Head_name=models.CharField(max_length=100)
    No_of_adults=models.IntegerField()
    no_of_children=models.IntegerField()
    Identity_no=models.CharField(max_length=100)
    Room_code=models.IntegerField()
    No_of_nights=models.IntegerField()
    
    
 

      


    

    
