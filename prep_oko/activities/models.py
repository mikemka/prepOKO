from django.db import models
from django.conf import settings


class ActivityType(models.Model):
    title = models.CharField(
        verbose_name='Название типа',
        max_length=127,
    )
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'тип активности'
        verbose_name_plural = 'типы активности'


class LevelType(models.Model):
    title = models.CharField(
        verbose_name='Название уровня',
        max_length=127,
    )
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'уровень'
        verbose_name_plural = 'уровни'


class Activity(models.Model):
    title = models.CharField(
        verbose_name='Название активности',
        max_length=255,
    )
    user = models.ForeignKey(
        verbose_name='Пользователь',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    activity_type = models.ForeignKey(
        verbose_name='Тип активности',
        to=ActivityType,
        on_delete=models.SET_NULL,
        null=True,
    )
    level_type = models.ForeignKey(
        verbose_name='Уровень',
        to=LevelType,
        on_delete=models.SET_NULL,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True,
    )
    checking_status = models.CharField(
        verbose_name='Статус проверки',
        max_length=31,
        choices=(
            ('pending', 'Ожидание'),
            ('accepted', 'Одобрено'),
            ('declined', 'Отклонено'),
        ),
        default='pending',
    )
    form = models.CharField(
        verbose_name='Класс',
        max_length=31,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True,
    )
    points_number = models.PositiveIntegerField(
        verbose_name='Количество баллов',
        default=0,
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'активность'
        verbose_name_plural = 'активности'
