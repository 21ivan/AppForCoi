from django.contrib import admin
from .models import Doctor, Direction


# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_name', 'slag', 'description')
    list_filter = ('experience', 'direction')
    list_editable = ('doctor_name',)
    list_display_links = ('description',)


admin.site.register(Direction)
admin.site.register(Doctor, DoctorAdmin)
