# Generated by Django 4.1.2 on 2022-11-06 15:06

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
                ('title', models.CharField(max_length=50, verbose_name='Название статьи')),
                ('data', models.DateTimeField(verbose_name='Дата публикации')),
                ('short_text', models.CharField(max_length=250, verbose_name='Краткое описание')),
                ('full_text', models.TextField(verbose_name='Полный текст новости')),
            ],
        ),
    ]
