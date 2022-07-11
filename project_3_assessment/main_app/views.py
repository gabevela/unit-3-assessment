# Create your views here.
from importlib.resources import contents
from pydoc import describe
import re
from django.shortcuts import render, redirect
# Add the following import
from django.http import HttpResponse, HttpRequest
from .models import Widget


# Define the home view
def home(request): #,widgets
    return render(request, 'home.html' )
    #, { 'widgets' : widgets }

def add(request):

    print("thank you for submitting a widgetttt ----------- ")
    
    added_widget = Widget(description = request.POST['description'], quantity = request.POST['quantity'])
    print(added_widget)
    added_widget.save()
    print('this is printing near the end')
    return render(request, 'home.html' )
    # return redirect('home.html')

  



def delete(request):
    return render(request, 'delete.html')



# mywidget = Widget.objects.create(widget = request.POST['widget'],
#                             quantity = request.POST['quantity']                          
#                             )