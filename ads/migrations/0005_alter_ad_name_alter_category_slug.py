# Generated by Django 4.1.3 on 2022-12-26 22:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_category_slug_alter_ad_is_published_alter_ad_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=10, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
