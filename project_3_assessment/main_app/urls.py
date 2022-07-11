from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add_widget'),

    path('delete/<int:widget_id>', views.delete, name='delete_widget'),

]

