# Generated by Django 3.2.8 on 2021-10-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_articles_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='tel',
            field=models.IntegerField(verbose_name='Телефон'),
        ),
    ]
