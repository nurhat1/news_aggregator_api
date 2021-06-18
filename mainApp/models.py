from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField('Название категории',  max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Категория {self.name}'


class Feed(models.Model):
    category = models.ForeignKey(Category, help_text='Категория', on_delete=models.CASCADE)
    name = models.CharField('Название ресурса', max_length=255)
    url = models.URLField('Ссылка на ресурс', max_length=255, unique=True)
    rss_link = models.TextField('RSS ссылка ресурса', max_length=255)

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'

    def __str__(self):
        return f'Ресурс {self.name}'
