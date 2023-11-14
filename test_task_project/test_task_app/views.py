from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


# Create your views here.


def get_employees(request):
    employees = Employee.objects.select_related('position')
    context = {'employees': employees}
    return render(request, 'test_task_app/employees/get_employees.html', context)


def add_employee(request):
    success_post = ''
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmployeeForm()
            success_post = 'Сотрудник успешно добавлен'
    elif request.method == 'GET':
        form = EmployeeForm()
    context = {'form': form, 'success_post': success_post}
    return render(request, 'test_task_app/employees/edit_employee.html', context)


def delete_employee(request, employee_id):
    Employee.objects.filter(id=employee_id).delete()
    return redirect(get_employees)


def update_employee(request, employee_id):
    instance = get_object_or_404(Employee, pk=employee_id)
    success_post = ''
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            form = EmployeeForm(instance=instance)
            success_post = 'Сотрудник успешно обновлен'
    elif request.method == 'GET':
        form = EmployeeForm(instance=instance)
    context = {'form': form, 'success_post': success_post}
    return render(request, 'test_task_app/employees/edit_employee.html', context)


def get_positions(request):
    positions = Position.objects.select_related()
    context = {'positions': positions}
    return render(request, 'test_task_app/position/get_positions.html', context)


def add_position(request):
    success_post = ''
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            form = PositionForm()
            success_post = 'Должность успешно добавлен'
    elif request.method == 'GET':
        form = PositionForm()
    context = {'form': form, 'success_post': success_post}
    return render(request, 'test_task_app/position/edit_position.html', context)


def delete_position(request, position_id):
    Position.objects.filter(id=position_id).delete()
    return redirect(get_positions)


def update_position(request, position_id):
    instance = get_object_or_404(Position, pk=position_id)
    success_post = ''
    if request.method == 'POST':
        form = PositionForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            form = PositionForm(instance=instance)
            success_post = 'Должность успешно обновлена'
    elif request.method == 'GET':
        form = PositionForm(instance=instance)
    context = {'form': form, 'success_post': success_post}
    return render(request, 'test_task_app/employees/edit_employee.html', context)
