# Generated by Django 5.0.1 on 2024-04-03 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_department_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumption',
            name='types',
            field=models.IntegerField(choices=[(1, 'gas'), (2, 'electracity'), (3, 'lands'), (4, 'water'), (5, 'wifi'), (6, 'not_gived')], default=6),
        ),
    ]