# Generated by Django 5.1.1 on 2024-09-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMS', '0011_vehical'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehical',
            name='vehical_type',
            field=models.CharField(choices=[('Two Wheeler', 'Two Wheeler'), ('Three Wheeler', 'Three Wheeler'), ('Four Wheeler', 'Four Wheeler')], max_length=40),
        ),
    ]
