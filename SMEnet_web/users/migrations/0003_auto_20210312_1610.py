# Generated by Django 3.1.6 on 2021-03-12 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210312_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='Application_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='hsme',
            name='End_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='hsme',
            name='Start_date',
            field=models.DateField(),
        ),
    ]
