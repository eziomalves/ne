# Generated by Django 3.0.7 on 2020-06-14 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='pro_descricao',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='pro_nome',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='pro_quantidade',
            new_name='quantidade',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='pro_valor',
            new_name='valor',
        ),
    ]