# Generated by Django 4.2.16 on 2024-09-25 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='Название типа')),
            ],
            options={
                'verbose_name': 'тип активности',
                'verbose_name_plural': 'типы активности',
            },
        ),
        migrations.CreateModel(
            name='LevelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='Название уровня')),
            ],
            options={
                'verbose_name': 'уровень',
                'verbose_name_plural': 'уровни',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название активности')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('checking_status', models.CharField(choices=[('pending', 'Ожидание'), ('accepted', 'Одобрено'), ('declined', 'Отклонено')], default='pending', max_length=31, verbose_name='Статус проверки')),
                ('form', models.CharField(max_length=31, verbose_name='Класс')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('points_number', models.PositiveIntegerField(default=0, verbose_name='Количество баллов')),
                ('activity_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='activities.activitytype', verbose_name='Тип активности')),
                ('level_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='activities.leveltype', verbose_name='Уровень')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'активность',
                'verbose_name_plural': 'активности',
            },
        ),
    ]
