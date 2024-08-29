# Generated by Django 5.1 on 2024-08-27 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=155, verbose_name="Заголовок")),
                ("full_name", models.CharField(max_length=155, verbose_name="ФИО")),
                ("image", models.ImageField(upload_to="base", verbose_name="Фото")),
                (
                    "image_main",
                    models.ImageField(upload_to="base/", verbose_name="Фото- 2"),
                ),
                ("job", models.CharField(max_length=155, verbose_name="Позиция")),
                (
                    "title_about",
                    models.CharField(max_length=155, verbose_name="Заголовка о нас"),
                ),
                ("descriptions_about", models.TextField(verbose_name="Описание О нас")),
                (
                    "image_abot",
                    models.ImageField(upload_to="image/", verbose_name="Фото о нас"),
                ),
                (
                    "title_team",
                    models.CharField(max_length=155, verbose_name="Заголовка Команды"),
                ),
                (
                    "descriptions_team",
                    models.TextField(verbose_name="Описание Команды"),
                ),
            ],
            options={
                "verbose_name_plural": "Настройка главной",
            },
        ),
    ]
