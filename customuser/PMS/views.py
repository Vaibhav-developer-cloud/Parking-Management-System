from django.shortcuts import render

# Create your views here.
from .serelizers import *
from .models import Building, Rows
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class BuildingView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializers


class FloorView(generics.ListCreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializers


class RowsView(generics.ListCreateAPIView):
    queryset = Rows.objects.all()
    serializer_class = RowSerializers

class ColumnView(generics.ListCreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializers


class VehicalView(generics.ListCreateAPIView):
    queryset = Vehical.objects.all()
    serializer_class = VehicalSerializers
