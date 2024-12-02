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
]