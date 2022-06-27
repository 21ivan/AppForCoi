from django.shortcuts import render
from .models import Doctor, Direction


# Create your views here.

def doctor_list(request):
    queryset = Doctor.objects.all().order_by('date_of_birthday', 'experience')
    content = {
        'title': 'Doctor List',
        'queryset': queryset
    }
    return render(request, 'doctors/doctors_list.html', content)


def direction_list(request):
    queryset = Direction.objects.all()
    content = {
        'title': 'Direction List',
        'queryset': queryset
    }
    return render(request, 'doctors/directions_list.html', content)
