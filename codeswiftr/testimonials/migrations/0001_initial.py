# Generated by Django 3.0.5 on 2020-06-24 08:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('content', models.CharField(max_length=200, verbose_name='content')),
                ('avatar', models.ImageField(upload_to='img/')),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='rating')),
            ],
        ),
        migrations.CreateModel(
            name='TestimonialsSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('subtitle', models.CharField(max_length=50, verbose_name='subtitle')),
                ('testimonials', models.ManyToManyField(to='testimonials.Testimonial', verbose_name='testimonials')),
            ],
        ),
    ]
