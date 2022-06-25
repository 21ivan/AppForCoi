from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('directions', DirectionViewSet)
router.register('doctors', DoctorViewSet)
#
# urlpatterns = [
#     path('', include('doctors.urls'))
# ]

urlpatterns = router.urls
