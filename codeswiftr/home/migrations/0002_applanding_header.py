# Generated by Django 3.0.5 on 2020-06-23 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_header', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applanding',
            name='header',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_header.AppDetails', verbose_name=''),
            preserve_default=False,
        ),
    ]
