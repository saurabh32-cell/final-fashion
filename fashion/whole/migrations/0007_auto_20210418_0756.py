# Generated by Django 3.1.7 on 2021-04-18 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whole', '0006_category_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
