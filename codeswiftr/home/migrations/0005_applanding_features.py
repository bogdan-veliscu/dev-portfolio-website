# Generated by Django 3.0.5 on 2020-06-24 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_features', '0002_auto_20200624_0810'),
        ('home', '0004_auto_20200624_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='applanding',
            name='features',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE,
                                       to='app_features.MainFeatures', verbose_name='features'),
            preserve_default=False,
        ),
    ]
