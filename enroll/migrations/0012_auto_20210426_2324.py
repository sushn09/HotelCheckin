# Generated by Django 3.2 on 2021-04-26 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0011_auto_20210426_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='intime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 26, 23, 24, 11, 651812)),
        ),
        migrations.AlterField(
            model_name='user',
            name='outtime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 26, 23, 24, 11, 651812)),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='myimage/AK.jpg', upload_to=''),
        ),
    ]
