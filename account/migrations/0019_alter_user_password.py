# Generated by Django 3.2.16 on 2023-01-28 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20230128_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=10, verbose_name='password'),
        ),
    ]
