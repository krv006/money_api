# Generated by Django 5.0.1 on 2024-03-23 21:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_plastic_card_debtors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plastic_card',
            name='Plastic_nmae',
        ),
        migrations.AddField(
            model_name='plastic_card',
            name='plastic_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.card'),
            preserve_default=False,
        ),
    ]
