# Generated by Django 5.0.7 on 2024-07-13 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0005_alter_cliente_ag_alter_cliente_bc_alter_cliente_cc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='tel',
            field=models.CharField(default='', max_length=13),
        ),
    ]
