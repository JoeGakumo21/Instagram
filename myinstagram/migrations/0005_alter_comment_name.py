# Generated by Django 3.2.8 on 2021-10-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinstagram', '0004_auto_20211017_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]