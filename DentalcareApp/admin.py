from django.contrib import admin
from .models import Appointment,Contact,ImageModel

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(ImageModel)
