# Generated by Django 5.0.1 on 2024-03-25 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_plastic_card_plastic_nmae_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camunalca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.IntegerField()),
                ('gas', models.IntegerField()),
                ('electricity', models.IntegerField()),
                ('wifi', models.IntegerField()),
                ('lands', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dollars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dollar', models.IntegerField()),
                ('dollar_course', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workers_salary_month', models.IntegerField()),
                ('workers_salary_weeks', models.IntegerField()),
                ('workers_salary_days', models.IntegerField()),
                ('workers_salary_oclocs', models.IntegerField()),
            ],
        ),
    ]
