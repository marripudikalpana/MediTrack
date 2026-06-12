from django.contrib import admin
from .models import Hospital

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'city',
        'phone'
    )

    search_fields = (
        'name',
        'city'
    )
# Register your models here.
