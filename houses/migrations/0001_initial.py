# Generated by Django 5.0.14 on 2025-06-16 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to='house_cards/', verbose_name='Превью дома')),
                ('price', models.CharField(max_length=100, verbose_name='Цена')),
                ('size', models.CharField(blank=True, max_length=250, null=True, verbose_name='Габариты')),
                ('photo_house', models.ImageField(blank=True, null=True, upload_to='houses/', verbose_name='Фото дома')),
                ('floor', models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество этажей')),
                ('total_area', models.CharField(blank=True, max_length=250, null=True, verbose_name='Строительная площадь')),
                ('bedroom', models.PositiveIntegerField(blank=True, null=True, verbose_name='Спальни')),
                ('bathroom', models.PositiveIntegerField(blank=True, null=True, verbose_name='Санузел')),
                ('living_room_area', models.CharField(blank=True, max_length=100, null=True, verbose_name='Площадь гостиной')),
                ('terrace_count', models.PositiveIntegerField(blank=True, null=True, verbose_name='Террасы и балконы')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Подробное описание')),
            ],
            options={
                'verbose_name': 'house',
                'verbose_name_plural': 'houses',
            },
        ),
        migrations.CreateModel(
            name='HousePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_image', models.ImageField(blank=True, null=True, upload_to='house_plans/', verbose_name='План дома и фасадов')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.house', verbose_name='План дома и фасадов')),
            ],
            options={
                'verbose_name': 'house_plan',
                'verbose_name_plural': 'house_plans',
                'ordering': ['order'],
            },
        ),
    ]
