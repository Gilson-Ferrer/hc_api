# Generated by Django 5.0.7 on 2024-07-13 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0003_cliente_remove_conjunto_roadmap_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='doc_1',
            new_name='cpf',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='doc_2',
            new_name='rg',
        ),
    ]
