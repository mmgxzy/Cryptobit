from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    full_name = models.CharField(
        max_length=155,
        verbose_name='ФИО'
    )
    logo = models.ImageField(
        upload_to='image/',
        verbose_name='Логотип'
    )
    image = models.ImageField(
        upload_to='base',
        verbose_name='Фото'
    )
    image_main = models.ImageField(
        upload_to='base/',
        verbose_name='Фото- 2'
    )
    job = models.CharField(
        max_length=155,
        verbose_name='Позиция'
    )
    title_about = models.CharField(
        max_length=155,
        verbose_name='Заголовка о нас'
    )
    descriptions_about = models.TextField(
        verbose_name='Описание О нас'
    )
    image_abot = models.ImageField(
        upload_to='image/',
        verbose_name='Фото о нас'
    )
    title_team =  models.CharField(
        max_length=155,
        verbose_name='Заголовка Команды'
    )
    descriptions_team = models.TextField(
        verbose_name='Описание Команды'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настройка главной'

class Image(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фото'
    )

    class Meta:
        verbose_name_plural = 'Фотография'

class Cryptobit(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    title2 = models.CharField(
        max_length=155,
        verbose_name='Заголовок2'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    vybor = models.CharField(
        max_length=30,
        verbose_name='задание'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настройка криптобит'

class Experts(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настройка рядом с экспертами'

class ExpertsFoto(models.Model):
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

class Story(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    data = models.DateField(
        auto_created=True,
        verbose_name='Дата'
    )
    order = models.CharField(
        max_length=155,
        verbose_name='порядок'
    )
    number = models.CharField(
        max_length=155,
        verbose_name='номер'
    )


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настройка истории'
    
class About(models.Model):
    banner = models.ImageField(
        upload_to='banner/',
        verbose_name='баннер'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    title_cryptobit = models.CharField(
        max_length=155,
        verbose_name='Заголовок криптобита'
    )
    descriptions = models.TextField(
        verbose_name='Описание криптобита'
    )
    foto_cryptobit = models.ImageField(
        upload_to='foto/',
        verbose_name='фото криптобита'
    )
    title_project = models.CharField(
        max_length=155,
        verbose_name='Заголовок проекта'
    )
    descriptions_project = models.TextField(
        verbose_name='Описание проекта '
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настройка другое'

    
class ProjectFoto(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фото проект'
    )

    class Meta:
        verbose_name_plural = 'Фотография проект'

class ArticlesFoto(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    data = models.DateField(
        auto_created=True,
        verbose_name='Дата'
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фото cтатьи'
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настройка статьи'


class Team(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='team/'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настойка инвистиции'