from django.urls import path, include
from rest_framework import routers
from .api import *
from doctors.views import *
router = routers.DefaultRouter()
router.register('directions/', DirectionViewSet)
router.register('doctors/', DoctorViewSet)

urlpatterns = [
    path('doctors/', doctor_list, name='doctors'),
    path('directions/', direction_list, name='directions'),

]

urlpatterns += router.urls
