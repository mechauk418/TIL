# Generated by Django 4.1.4 on 2023-03-28 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hits',
            field=models.IntegerField(default=0, verbose_name='조회수'),
        ),
    ]
