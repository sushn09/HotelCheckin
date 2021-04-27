# Generated by Django 3.2 on 2021-04-27 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0012_auto_20210426_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='amount',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='intime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 11, 44, 54, 212151)),
        ),
        migrations.AlterField(
            model_name='user',
            name='outtime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 11, 44, 54, 212151)),
        ),
        migrations.AlterField(
            model_name='user',
            name='paymethod',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='myimage/AK.jpg', upload_to='myimage/'),
        ),
    ]