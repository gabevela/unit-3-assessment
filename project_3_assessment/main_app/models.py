from django.db import models
from django.urls import reverse

# Create your models here.
class Widget:  # Note that parens are optional if not inheriting from another class
  def __init__(self, description, quantity):
    
    self.description = description
    self.quantity = quantity

widgets = [
  Widget('THIS IS THE DESCRIPTION', 4)
]
