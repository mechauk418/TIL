# Generated by Django 4.1.4 on 2023-04-04 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_remove_postimage_image_resize_alter_postimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='image_original',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]