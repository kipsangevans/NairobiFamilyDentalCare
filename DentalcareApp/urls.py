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
    path('our team/', views.ourteam, name='our-team'),
]