from datetime import date

from django.db import models
from django.urls import reverse

from webapp.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=200, verbose_name='Статус')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(models.Model):
    name = models.CharField(max_length=300, verbose_name='Тип')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Task(models.Model):
    summary = models.CharField(max_length=255, null=False, blank=False, verbose_name='Заголовок',
                               validators=(MinLengthValidator(2),))
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание',
                                   validators=(MaxLengthValidator(2000),))
    status = models.ForeignKey('webapp.Status', related_name='tasks', on_delete=models.PROTECT, verbose_name='Статус')
    type = models.ManyToManyField('webapp.Type', related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    project = models.ForeignKey('webapp.Project', related_name='tasks', on_delete=models.CASCADE, verbose_name='Проект')

    def __str__(self):
        return f"{self.pk}.{self.summary}"

    class Meta:
        db_table = 'tasks'
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'


class Project(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    date_start = models.DateField(default=date.today, verbose_name='Дата начала')
    date_end = models.DateField(null=True, blank=True, verbose_name="Дата окончания")

    def get_absolute_url(self):
        return reverse("webapp:project_view", kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'projects'
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'