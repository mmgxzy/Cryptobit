from django.db import models

class Blog(models.Model):
    banner = models.ImageField(
        upload_to='banner/',
        verbose_name='баннер'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='заголовок'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='фото'
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='дата'
    )
    title_cryptobit = models.CharField(
        max_length=155,
        verbose_name='Заголовок криптобита'
    )
    descriptions = models.TextField(
        verbose_name='Описание криптобита'
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настройка блога'

class Story(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='заголовок'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='фото'
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='дата'
    )
    descriptions = models.TextField(
        verbose_name='Описание криптобита'
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настройка сториса'

class Experts(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фото'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    descriptions = models.TextField(
        verbose_name='Ноправление'
    )
    facebook = models.URLField(
        verbose_name='Укжите ссылку на facebook'
    )
    chtoto = models.URLField(
        verbose_name='Укжите ссылку на chtoto'
    )
    twitter = models.URLField(
        verbose_name='Укжите ссылку на twitter'
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настройка экспертов'