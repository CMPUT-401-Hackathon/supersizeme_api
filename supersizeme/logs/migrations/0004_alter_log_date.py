# Generated by Django 3.2.7 on 2021-09-12 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_alter_log_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(),
        ),
    ]
