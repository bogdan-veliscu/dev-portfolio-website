# Generated by Django 3.0.5 on 2020-06-23 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_header', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appdetails',
            old_name='actionTitle',
            new_name='action_title',
        ),
        migrations.AddField(
            model_name='appdetails',
            name='action_url',
            field=models.CharField(default='Download', max_length=100),
            preserve_default=False,
        ),
    ]
