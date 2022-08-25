# Generated by Django 4.0.6 on 2022-08-25 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='country',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('opening_date', models.DateField()),
                ('running_time', models.IntegerField()),
                ('screening', models.BooleanField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.director')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.genre')),
            ],
        ),
    ]
