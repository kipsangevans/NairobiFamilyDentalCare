from django.contrib import admin
from django.urls import path
from DentalcareApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starterpage'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('appointment/', views.appointment, name='appointment'),
    path('virtual-consultation/', views.virtual, name='virtual-consultation'),
    #
    # upload image
    path('uploadimage/', views.upload_image, name='upload'),
    path('our team/', views.our_team, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard_appointments/', views.appointments_dashboard, name='appointments_dashboard'),
    path('confirm/<int:id>/', views.confirm_appointment, name='confirm_appointment'),
    path('deleteAppointment/<int:id>', views.deleteAppointment, name="deleteAppointment"),

]
