# Generated by Django 3.0.7 on 2020-06-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20200614_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
