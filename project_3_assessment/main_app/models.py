from django.db import models
from django.urls import reverse

class Widget(models.Model):  
    
    description = models.CharField(max_length=150, default="1")
    quantity = models.CharField(max_length=150 ,default="2")
    

