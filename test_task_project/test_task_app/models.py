from django.db import models


# Create your models here.
class Employee(models.Model):
    last_name = models.CharField(max_length=60, verbose_name='Фамилия сотрудника')
    patronymic = models.CharField(max_length=60, null=True, verbose_name='Отчество сотрудника')
    first_name = models.CharField(max_length=60, verbose_name='Имя сотрудника')
    position = models.ForeignKey('Position', on_delete=models.PROTECT, verbose_name='Должность')
    date_accept = models.DateField(verbose_name='Дата принятия сотрудника на работу')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.get_fio

    @property
    def get_fio(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'


class Position(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название должности')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name
