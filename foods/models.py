from django.db import models
from datetime import date

# Create your models here.
class Food(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=50)
  rate = models.IntegerField(default=0)
  price =  models.IntegerField()
  time = models.IntegerField()
  pub_date = models.DateField(auto_now=False, auto_now_add=True)
  photo = models.ImageField(upload_to='foods/')
  
  def __str__(self):
    return self.name
