# Generated by Django 3.1.6 on 2021-04-16 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('L_id', models.IntegerField()),
                ('Application_date', models.DateField()),
                ('H_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hsme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('H_id', models.IntegerField()),
                ('Company', models.CharField(max_length=20)),
                ('Sector', models.CharField(max_length=20)),
                ('Location', models.CharField(max_length=20)),
                ('No_of_employees_required', models.IntegerField()),
                ('Years', models.IntegerField()),
                ('Ready', models.CharField(max_length=10)),
                ('Start_date', models.DateField()),
                ('End_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Lsme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('L_id', models.IntegerField()),
                ('Company', models.CharField(max_length=20)),
                ('Sector', models.CharField(max_length=20)),
                ('Location', models.CharField(max_length=20)),
                ('No_of_employees_being_laid_off', models.IntegerField()),
                ('Laid_off', models.IntegerField()),
            ],
        ),
    ]
