# Generated by Django 3.1.7 on 2021-04-18 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0004_auto_20210418_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='static/uploads'),
        ),
    ]
