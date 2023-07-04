from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES={
   ('WO', 'WOMEN'),
    ('ME', 'MEN'),
    ('KI', 'KID'),
}







class Product(models.Model):
    title= models.CharField(max_length=100)
    selling_price= models.FloatField()
    discounted_price= models.FloatField()
    description= models.TextField()
    composition= models.TextField(default='')
    prodapp= models.TextField(default='')
    category= models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image= models.ImageField(null= True , blank= True)
def _str_(self):
 return self.title


class Cart(models.Model):
   user= models.ForeignKey(User,on_delete=models.CASCADE)
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity = models.PositiveIntegerField(default=1)

   @property
   def total_cost(self):
     return self.quantity * self.product.disconted_price
   


STATUS_CHOICES = {
   ('Accepted','Accepted'),
   ('Packed','Packed'),
   ('On The Way','On The Way'),
   ('Deliverd','Delivered'),
   ('Cancel','Cancel'),
   ('Pending','Pending'),
}




class Payment(models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      amount = models.FloatField()
      razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
      razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
      razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
      paid = models.BooleanField(default=False)
   


class OrderPlaced(models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      product = models.ForeignKey(Product,on_delete=models.CASCADE)
      quantity= models.PositiveIntegerField(default=1)
      ordered_date = models.DateTimeField(auto_now_add=True)
      status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='Pending')
      payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
      @property
      def _total_cost(self):
         return self.quantity * self.product.discounted_price
         
   


   