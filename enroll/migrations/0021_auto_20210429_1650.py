# Generated by Django 3.2 on 2021-04-29 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0020_auto_20210429_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='indate',
            field=models.DateField(default=datetime.datetime(2021, 4, 29, 16, 50, 45, 400363)),
        ),
        migrations.AddField(
            model_name='user',
            name='outdate',
            field=models.DateField(default=datetime.datetime(2021, 4, 29, 16, 50, 45, 400363)),
        ),
        migrations.AddField(
            model_name='user',
            name='room',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='user',
            name='intime',
            field=models.TimeField(default=datetime.datetime(2021, 4, 29, 16, 50, 45, 400363)),
        ),
        migrations.AlterField(
            model_name='user',
            name='outtime',
            field=models.TimeField(default=datetime.datetime(2021, 4, 29, 16, 50, 45, 400363)),
        ),
    ]