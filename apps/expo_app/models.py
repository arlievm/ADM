from django.db import models

from apps.main_page.models import Category
from .services import get_upload_path, validate_file_extension
from .choices import STATUS


class Location(models.Model):

    class Meta:
        db_table = 'locations'
        verbose_name = 'location'
        verbose_name_plural = 'locations'

    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    address = models.CharField(verbose_name="Адресс", max_length=32)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    location = models.CharField(verbose_name='Ссылка для локации', max_length=256, blank=True, null=True)
    image = models.ImageField(verbose_name='Фотография', validators=[validate_file_extension], upload_to=get_upload_path, null=True, blank=True)

    def __str__(self):
        return self.address
    

class Hotel(models.Model):

    class Meta:
        db_table = 'hotel'
        verbose_name = 'Гостиница'
        verbose_name_plural = 'Гостиница'
    
    name = models.CharField(verbose_name="Название", max_length=64)
    image = models.ImageField(verbose_name="Фотография", )
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    ulr = models.URLField(verbose_name="Укажите *url сайта", blank=True, null=True)
    location = models.URLField(verbose_name="Укажите *url локации", blank=True, null=True)

    def __str__(self):
        return self.name


class Stand(models.Model):

    class Meta:
        db_table = 'stand'
        verbose_name = 'ОПЦИИ ВЫСТАВОЧНЫХ СТЕНДОВ'
        verbose_name_plural = 'ОПЦИИ ВЫСТАВОЧНЫХ СТЕНДОВ'

    status = models.CharField(verbose_name='Тип стендов', max_length=32, choices=STATUS, default=None)
    square = models.CharField(verbose_name='Площадь', max_length=16, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.CharField(verbose_name='', max_length=16, null=True, blank=True)

    def __str__(self):
        return self.status
    

class Feedback(models.Model):

    class Meta:
        db_table = 'feedback'
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    name = models.CharField(verbose_name="Ф.И.О", max_length=64)
    mail = models.EmailField(verbose_name="Почта", max_length=64)
    phone = models.CharField(verbose_name='Номер телефона', max_length=16)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return self.name


class Contacts(models.Model):

    class Meta:
        db_table = 'contacts'
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    phone = models.CharField(verbose_name='Номер телефона', max_length=16)
    mail = models.EmailField(verbose_name="Почта", max_length=64)
    address_ru = models.CharField(verbose_name='Адрес', max_length=64)
    address_en = models.CharField(verbose_name='Адрес', max_length=64)