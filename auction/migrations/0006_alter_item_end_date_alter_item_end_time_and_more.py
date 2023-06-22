# Generated by Django 4.1.2 on 2022-12-16 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='item',
            name='end_time',
            field=models.TimeField(default=datetime.time(23, 59, 59, 999999)),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='', upload_to='auction/frontend/public/'),
        ),
    ]
