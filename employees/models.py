from datetime import datetime
from django.db import models


def upload_photo_to(instance, filename):
    # TODO: file format and size validation? / ImageField
    print(instance, filename)
    new_string = f'{datetime.now()}_{filename}'
    return new_string


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name='Department name')
    head = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='employee',
                             verbose_name='Department head')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    # def __str__(self):
    #     return f'{self.name} (head: {self.head.id})'


class Employee(models.Model):
    POSITION_CHOICES = (
        (1, 'Стажер'),
        (2, 'Сотрудник'),
        (3, 'Зам.нач'),
        (4, 'Начальник'),
    )

    name_first = models.CharField(max_length=100, verbose_name='Имя')
    name_second = models.CharField(max_length=100, verbose_name='Фамилия')
    name_middle = models.CharField(max_length=100, verbose_name='Отчество')
    photo = models.ImageField(upload_to=upload_photo_to, blank=True, null=True, verbose_name='Фото')
    age = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Возраст')

    position = models.PositiveSmallIntegerField(choices=POSITION_CHOICES, null=True, blank=True)
    salary = models.DecimalField(max_digits=11, decimal_places=2)

    dept = models.ForeignKey(Department, on_delete=models.SET_NULL,
                             null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        unique_together = ['name_first', 'name_second', 'name_middle', 'dept']

    # def __str__(self):
    #     return f'surn:{self.name_second} pos:{self.position} dpt:{self.dept}'
