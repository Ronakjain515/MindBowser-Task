# Generated by Django 3.1.7 on 2021-02-20 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task_App', '0005_auto_20210220_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
