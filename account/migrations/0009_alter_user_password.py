# Generated by Django 3.2.16 on 2023-01-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=20, verbose_name='password'),
        ),
    ]
