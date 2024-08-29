# Generated by Django 5.1 on 2024-08-29 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_blog_banner"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="descriptions",
            field=models.TextField(default=1, verbose_name="Описание криптобита"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="blog",
            name="title_cryptobit",
            field=models.CharField(
                default=1, max_length=155, verbose_name="Заголовок криптобита"
            ),
            preserve_default=False,
        ),
    ]