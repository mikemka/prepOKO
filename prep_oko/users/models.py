from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import ImageField


class StudentsForm(models.Model):
    title = models.CharField(max_length=31, verbose_name='Название класса')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'класс'
        verbose_name_plural = 'классы'


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = ImageField(upload_to='avatars', null=True, blank=True)
    is_moderator = models.BooleanField(default=False)
    students_forms = models.ManyToManyField(
        StudentsForm,
        blank=True,
    )
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
