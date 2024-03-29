# Generated by Django 3.2.9 on 2023-06-07 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorEN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Спонсорство',
                'verbose_name_plural': 'Спонсорство',
                'db_table': 'sponsor_en',
            },
        ),
        migrations.CreateModel(
            name='MembersEN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='apps/members/images/', verbose_name='ФОТОГРАФИЯ *(125x125)')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Преимущества для участников',
                'verbose_name_plural': 'Преимущества для участников',
                'db_table': 'members_table_en',
            },
        ),
        migrations.CreateModel(
            name='AttributeSponsorsEN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='apps/members/images/', verbose_name='ФОТОГРАФИЯ *(125x125)')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members_en.sponsoren', verbose_name='Спонсор')),
            ],
            options={
                'verbose_name': 'Преимущества для спонсорства',
                'verbose_name_plural': 'Преимущества для спонсорства',
                'db_table': 'attribute_sponsors_en',
            },
        ),
    ]
