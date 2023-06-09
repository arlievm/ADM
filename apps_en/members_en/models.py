from django.db import models

from apps.main_page.models import Category


class MembersEN(models.Model):

    class Meta:
        db_table = 'members_table_en'
        verbose_name = 'Преимущества для участников'
        verbose_name_plural = 'Преимущества для участников'

    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="ФОТОГРАФИЯ *(125x125)", upload_to="apps/members/images/")
    title = models.CharField(verbose_name="Название", max_length=128)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.title
    

class SponsorEN(models.Model):

    class Meta: 
        db_table = 'sponsor_en'
        verbose_name = 'Спонсорство'
        verbose_name_plural = 'Спонсорство'

    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Название", max_length=128)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.title
    

class AttributeSponsorsEN(models.Model):

    class Meta:
        db_table = 'attribute_sponsors_en'
        verbose_name = 'Преимущества для спонсорства'
        verbose_name_plural = 'Преимущества для спонсорства'

    sponsor = models.ForeignKey(SponsorEN, verbose_name="Спонсор", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="ФОТОГРАФИЯ *(125x125)", upload_to="apps/members/images/")
    title = models.CharField(verbose_name="Название", max_length=128)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.title