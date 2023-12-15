from django.db import models
from datetime import date

# Create your models here.
class Food(models.Model):
  FOOD_TYPE = (
  ('drinks', 'Drinks'),
  ('dinner', 'Dinner'),
  ('lunch', 'Lunch'),
)
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=50)
  rate = models.IntegerField(default=0)
  price =  models.IntegerField()
  time = models.IntegerField()
  pub_date = models.DateField(auto_now=False, auto_now_add=True)
  photo = models.ImageField(upload_to='foods/')
  type_food = models.CharField(max_length=10,choices=FOOD_TYPE,default="drinks")
  
  def __str__(self):
    return self.name
