from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product')

    def __str__(self) -> str:
        return self.name
    

class Cart(models.Model):
    id = models.UUIDField(default = uuid.uuid4,primary_key = True)
    user =   models.ForeignKey(User,on_delete = models.CASCADE)  
    completed = models.BooleanField(default = False)


    def __str__(self) -> str:
        return self.id
    

class cartItems(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE,related_name = "item")  
    cart = models.ForeignKey(Cart,on_delete = models.CASCADE,related_name = "cartitems")  
    quantity = models.IntegerField(default = 0)

    def __str__(self) -> str:
        return self.name
    