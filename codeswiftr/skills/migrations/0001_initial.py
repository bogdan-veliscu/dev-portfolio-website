# Generated by Django 3.0.3 on 2020-04-17 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('linkedin_verified', models.BooleanField(default=False)),
                ('upsight_score', models.IntegerField(default=0)),
                ('linkedin_endorsments', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField(default=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
