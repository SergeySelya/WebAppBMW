# Generated by Django 3.2.8 on 2021-10-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='tel',
            field=models.IntegerField(max_length=13, verbose_name='Телефон'),
        ),
    ]