# Generated by Django 3.2.16 on 2023-01-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20230128_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(blank=True, max_length=30, verbose_name='password2'),
        ),
    ]
