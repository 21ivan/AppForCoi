from django.shortcuts import render
from .serializers import DirectionSerializer, DoctorSerializer
from .models import Doctor, Direction
from rest_framework import viewsets


# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DirectionViewSet(viewsets.ModelViewSet):
    serializer_class = DirectionSerializer
    queryset = Direction.objects.all()
