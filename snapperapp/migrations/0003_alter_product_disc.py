# Generated by Django 5.0.6 on 2024-06-17 06:38

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snapperapp', '0002_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='disc',
            field=tinymce.models.HTMLField(),
        ),
    ]
