# Generated by Django 3.0.5 on 2020-06-28 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_screens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appscreens',
            name='screens',
            field=models.ManyToManyField(to='app_screens.Screenshot', verbose_name='screens'),
        ),
    ]
