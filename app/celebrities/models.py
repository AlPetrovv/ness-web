from django.db import models
from django.utils.text import gettext_lazy as _


class Celebrity(models.Model):
    name = models.CharField(_('Имя Фамилия'), max_length=100)
    born_date = models.DateField(_('Дата рождения'))
    character = models.CharField(_('Характер'), max_length=50)
    energy = models.CharField(_('Энергия'), max_length=50)
    interest = models.CharField(_('Интерес'), max_length=50)
    health = models.CharField(_('Интерес'), max_length=50)
    logic = models.CharField(_('Логика'), max_length=50)
    work = models.CharField(_('Знак труда'), max_length=50)
    lucky = models.CharField(_('Везение'), max_length=50)
    sence_humor = models.CharField(_('Чувство юмора'), max_length=50)
    memory = models.CharField(_('Память'), max_length=50)
