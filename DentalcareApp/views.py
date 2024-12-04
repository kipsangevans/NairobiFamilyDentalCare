from datetime import timezone
from urllib import request

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import ImageUploadForm
from .models import Appointment, Contact, ImageModel


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

            name = request.POST.get('name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            date = request.POST.get('date'),
            time = request.POST.get('time'),
            doctor = request.POST.get('doctor'),
            message = request.POST.get('message'),
        )
        myappointment.save()
        return render(request, 'appointment.html', {'success_message': 'Your message has been sent.'})
    else:


          return render(request, 'appointment.html')
def virtual(request):
    return render(request,'virtual-consultation.html')

def ourteam(request):
    return render(request,'our-team.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/our team')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def our_team(request):
    images = ImageModel.objects.all()
    return render(request, 'our-team.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')

def dashboard(request):
    appointment_count = Appointment.objects.count()
    contact_count = Contact.objects.count()
    contacts = Contact.objects.order_by('-contact_time')[:5]


    appointments = Appointment.objects.order_by('-appointment_time')[:5]



    context = {
        'appointment_count': appointment_count,
        'appointments': appointments,
        'contact_count': contact_count,
        'contacts': contacts,
    }
    return render(request,'index.html', context)


def appointments_dashboard(request):
    appointments = Appointment.objects.filter(confirmed=False).order_by('-appointment_time')
    confirmed_appointments = Appointment.objects.filter(confirmed=True).order_by('-appointment_time')
    context = {
        'appointments': appointments,
        'confirmed_appointments': confirmed_appointments,

    }
    return render(request, 'appointments-dash.html',context)


def confirm_appointment(request,id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.confirmed = True  # Mark as confirmed
    appointment.save()
    return redirect('appointments_dashboard')

def deleteAppointment(request, id):
    Appointment.objects.get(id=id).delete()
    return redirect('appointments_dashboard')

def edit(request,id):
    editappointment = Appointment.objects.get(id=id)
    return render(request,'edit.html',{'appointment':editappointment})

