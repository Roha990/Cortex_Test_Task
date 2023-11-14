from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('employees/', get_employees, name='get_employees'),
    path('employees/add', add_employee, name='add_employee'),
    path('employees/delete/<int:employee_id>', delete_employee, name='delete_employee'),
    path('employees/update/<int:employee_id>', update_employee, name='update_employee'),
    path('positions/', get_positions, name='get_positions'),
    path('positions/add', add_position, name='add_position'),
    path('positions/delete/<int:position_id>', delete_position, name='delete_position'),
    path('positions/update/<int:position_id>', update_position, name='update_position'),
]