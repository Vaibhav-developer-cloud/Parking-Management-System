# Generated by Django 5.1.1 on 2024-09-27 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMS', '0007_building_total_columns_column'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='total_floors',
            field=models.IntegerField(default=2),
        ),
    ]
