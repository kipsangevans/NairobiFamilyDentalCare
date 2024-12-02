from urllib import request

from django.shortcuts import render
from django.http import HttpResponse
from .models import  Appointment,Contact



# Create your views here.
def index(request):
    return render(request,'indexx.html')
def starter(request):
    return render(request,'startpage.html')

def contact(request):
    if request.method == "POST":
        mycontact = Contact(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        mycontact.save()
        return render(request, 'contact.html', {'success_message': 'Your message has been sent.'})
    else:
        return render(request,'contact.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def appointment(request):

    if request.method == 'POST':
        myappointment=Appointment(

            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            time = request.POST['time'],
            doctor = request.POST['doctor'],
            message = request.POST['message']
        )
        myappointment.save()
        return render(request, 'contact.html', {'success_message': 'Your message has been sent.'})
    else:


          return render(request, 'appointment.html')
def virtual(request):
    return render(request,'virtual-consultation.html')

def ourteam(request):
    return render(request,'our-team.html')

