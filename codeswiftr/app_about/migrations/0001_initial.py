# Generated by Django 3.0.5 on 2020-06-24 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_features', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='subtitle')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
                ('top_features', models.ManyToManyField(to='app_features.AppFeature', verbose_name='features')),
            ],
        ),
    ]
