# Generated by Django 5.0.1 on 2024-04-03 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_consumption_types'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consumption',
            old_name='types',
            new_name='types_camunalca',
        ),
    ]
