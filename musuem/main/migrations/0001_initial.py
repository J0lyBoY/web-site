# Generated by Django 4.1.2 on 2022-11-01 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
                ('short_text', models.CharField(max_length=150, verbose_name='Описание новости')),
                ('full_text', models.TextField(verbose_name='Текст новости')),
            ],
        ),
    ]
