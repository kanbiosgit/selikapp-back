# Generated by Django 3.1.7 on 2021-04-08 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospecting', '0002_negociator_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='route',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
