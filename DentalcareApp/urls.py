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
    path('dashboard_contacts/', views.contacts_dashboard, name='contacts_dashboard'),
    path('confirm/<int:id>/', views.confirm_appointment, name='confirm_appointment'),
    path('deleteAppointment/<int:id>', views.deleteAppointment, name="deleteAppointment"),
    path('edit/<int:id>', views.edit, name="editAppointment"),
    path('update/<int:id>/', views.update, name='update'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('login_admin/', views.admin_login, name='admin_login'),
    path('logout/', views.user_logout, name='logout'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile_detail', views.profile_detail, name='profile_detail'),

]
