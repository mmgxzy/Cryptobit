# Generated by Django 5.1 on 2024-08-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_story"),
    ]

    operations = [
        migrations.CreateModel(
            name="Experts",
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
                ("image", models.ImageField(upload_to="image/", verbose_name="Фото")),
                ("title", models.CharField(max_length=155, verbose_name="Имя")),
                ("descriptions", models.TextField(verbose_name="Ноправление")),
                ("facebook", models.URLField(verbose_name="Укжите ссылку на facebook")),
                ("chtoto", models.URLField(verbose_name="Укжите ссылку на chtoto")),
                ("twitter", models.URLField(verbose_name="Укжите ссылку на twitter")),
            ],
            options={
                "verbose_name_plural": "Настройка экспертов",
            },
        ),
        migrations.AlterModelOptions(
            name="story",
            options={"verbose_name_plural": "Настройка сториса"},
        ),
    ]