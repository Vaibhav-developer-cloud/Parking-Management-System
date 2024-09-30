from django.db import models
from app.models import User


# Create your models here.

class Building(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    total_floors = models.IntegerField(default=2)
    total_rows = models.IntegerField(default=10)
    total_columns = models.PositiveIntegerField()


class Floor(models.Model):
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor_name = models.CharField(max_length=40)


class Rows(models.Model):
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor_id = models.ForeignKey(Floor,on_delete=models.CASCADE)
    Row_name = models.CharField(max_length=50)
    # total_rows = models.PositiveIntegerField()
    # building_name = models.CharField(max_length=50)
    # address = models.TextField(max_length=100)
    # total_rows = models.IntegerField(default=10)


class Column(models.Model):
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor_id = models.ForeignKey(Floor,on_delete=models.CASCADE)
    row_id = models.ForeignKey(Rows,on_delete=models.CASCADE)
    column_name = models.CharField(max_length=40)


class Vehical(models.Model):
    Types = (
        ("Two Wheeler", 'Two Wheeler'),
        ("Three Wheeler", 'Three Wheeler'),
        ("Four Wheeler", 'Four Wheeler')
    )

    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    vehical_name = models.CharField(max_length=100)
    vehical_type = models.CharField(choices=Types,max_length=40)
    vehical_no = models.CharField(max_length=40)
