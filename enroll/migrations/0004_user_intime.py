# Generated by Django 3.2 on 2021-04-25 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_auto_20210425_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='intime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
