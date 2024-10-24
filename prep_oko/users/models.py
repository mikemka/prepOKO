from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import ImageField


class StudentsForm(models.Model):
    title = models.CharField(max_length=31, verbose_name='Название класса')


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = ImageField(upload_to='avatars', null=True, blank=True)
    is_moderator = models.BooleanField(default=False)
    students_forms = models.ManyToManyField(
        StudentsForm,
        blank=True,
    )
