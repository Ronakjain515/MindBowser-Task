# Generated by Django 3.1.7 on 2021-02-20 13:00

import Task_App.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task_App', '0004_auto_20210220_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(max_length=10, validators=[Task_App.validators.MobileNoValidator]),
        ),
    ]
