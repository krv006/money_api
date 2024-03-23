# Generated by Django 5.0.1 on 2024-03-23 20:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='Plastic_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('Plastic_nmae', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.card')),
            ],
        ),
        migrations.CreateModel(
            name='Debtors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('phone_numuber', models.CharField(blank=True, max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=11)),
                ('product', models.ManyToManyField(to='core.product')),
            ],
        ),
    ]
