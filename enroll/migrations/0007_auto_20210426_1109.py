# Generated by Django 3.2 on 2021-04-26 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0006_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='guests',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='intime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 26, 11, 9, 52, 347664)),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobileno',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='nightstay',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='outtime',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='paymethod',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(upload_to='myimage'),
        ),
    ]