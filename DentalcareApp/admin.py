from django.contrib import admin
from .models import Appointment,Contact,ImageModel

# Register your models here.
from .models import PatientProfile

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'phone_number', 'updated_at')
    search_fields = ('user__username', 'phone_number')
admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(ImageModel)
