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
    widget = {"widgets_list" : Widget.objects.all()}
    return render(request, 'home.html', widget )
    #, { 'widgets' : widgets }

def add(request):

    print("thank you for submitting a widgetttt ----------- ")
    
    added_widget = Widget(description = request.POST['description'], quantity = request.POST['quantity'])
    print(added_widget)
    added_widget.save()
    print('this is printing near the end')
    #Return render(request, 'home.html' )
    return redirect('/')

def delete(request, widget_id):
    widget_delete = Widget.objects.get(id = widget_id )
    widget_delete.delete()
    return redirect('/')

    #return render(request, 'delete.html')

