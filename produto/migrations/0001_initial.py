# Generated by Django 3.0.7 on 2020-06-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_nome', models.CharField(max_length=255)),
                ('pro_valor', models.DecimalField(decimal_places=2, max_digits=3)),
                ('pro_quantidade', models.PositiveIntegerField()),
                ('pro_descricao', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
