from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate


class BuildingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"
        # exclude = ["name"]


class RowSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rows
        fields = "__all__"


class FloorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = "__all__"


class ColumnSerializers(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = "__all__"


class VehicalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehical
        fields = "__all__"