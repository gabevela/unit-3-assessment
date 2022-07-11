from django.db import models
from django.urls import reverse

# Create your models here.
class Widget(models.Model):  # Note that parens are optional if not inheriting from another class
    description = models.TextField()
    quantity = models.IntegerField()
    

#   def __init__(self, description, quantity):
    
#     self.description = description
#     self.quantity = quantity

# widgets = [
#   Widget('THIS IS THE DESCRIPTION', 4)
# ]
