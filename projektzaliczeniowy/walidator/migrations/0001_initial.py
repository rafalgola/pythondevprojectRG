# Generated by Django 4.2 on 2024-05-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asserted_Pesels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp', models.CharField(max_length=16)),
                ('pesel', models.CharField(max_length=11)),
                ('assertion_result', models.CharField(max_length=5)),
            ],
        ),
    ]
