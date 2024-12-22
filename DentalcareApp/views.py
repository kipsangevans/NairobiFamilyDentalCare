from datetime import timezone
from django.contrib import messages
from urllib import request
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


from .forms import ImageUploadForm, AppointmentForm,PatientProfileForm
from .models import Appointment, Contact, ImageModel,PatientProfile


# Create your views here.
def index(request):
    return render(request, 'indexx.html')


def starter(request):
    return render(request, 'startpage.html')


def contact(request):
    if request.method == "POST":
        mycontact = Contact(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        mycontact.save()
        return render(request, 'contact.html', {'success_message': 'Your message has been sent.'})
    else:
        return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def appointment(request):
    if request.method == 'POST':
        myappointment = Appointment(

            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            date=request.POST.get('date'),
            time=request.POST.get('time'),
            doctor=request.POST.get('doctor'),
            message=request.POST.get('message'),
        )
        myappointment.save()
        return render(request, 'appointment.html', {'success_message': 'Your message has been sent.'})
    else:

        return render(request, 'appointment.html')


def virtual(request):
    return render(request, 'virtual-consultation.html')


def ourteam(request):
    return render(request, 'our-team.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image')  # Adjust the redirect URL as needed
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

@login_required
def dashboard(request):
    appointment_count = Appointment.objects.count()
    contact_count = Contact.objects.count()
    contacts = Contact.objects.order_by('-contact_time')[:5]
    user_count = User.objects.filter(is_staff=False).count()
    user_count_admin = User.objects.filter(is_staff=True).count()

    appointments = Appointment.objects.order_by('-appointment_time')[:5]

    context = {
        'appointment_count': appointment_count,
        'appointments': appointments,
        'contact_count': contact_count,
        'contacts': contacts,
        'user_count': user_count,
        'user_count_admin': user_count_admin,
    }
    return render(request, 'index.html', context)


def appointments_dashboard(request):
    appointments = Appointment.objects.filter(confirmed=False).order_by('-appointment_time')
    confirmed_appointments = Appointment.objects.filter(confirmed=True).order_by('-appointment_time')
    context = {
        'appointments': appointments,
        'confirmed_appointments': confirmed_appointments,

    }
    return render(request, 'appointments-dash.html', context)


def contacts_dashboard(request):
    contacts = Contact.objects.order_by('-contact_time')[:5]
    context = {
        'contacts': contacts,
    }

    return render(request, 'contact-dash.html', context)


def confirm_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.confirmed = True  # Mark as confirmed
    appointment.save()
    return redirect('appointments_dashboard')


def deleteAppointment(request, id):
    Appointment.objects.get(id=id).delete()
    return redirect('appointments_dashboard')


def edit(request, id):
    editappointment = Appointment.objects.get(id=id)
    return render(request, 'edit.html', {'appointment': editappointment})


def update(request, id):
    updateappointment = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST, instance=updateappointment)
    if form.is_valid():
        form.save()
        return redirect('appointments_dashboard')
    else:
        return render(request, 'edit.html')


def register(request):
    # if request.method == 'POST':
    #     members = Member(
    #         name = request.POST['name'],
    #
    #         username = request.POST['username'],
    #         password = request.POST['password'],
    #     )
    #     members.save()
    #     return redirect('/login')
    # else:
    return render(request, 'register.html')




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, 'Both username and password are required!')
            return render(request, 'login.html')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password!')

    return render(request, 'login.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, 'Both username and password are required!')
            return render(request, 'login.html')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:
                auth_login(request, user)

                return redirect('dashboard')
            else:
                messages.error(request, 'You are not authorized to log in as staff.')
        else:
            messages.error(request, 'Invalid username or password!')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login')

    return render(request, 'register.html')

def user_logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')



def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():

            messages.success(request, 'Password reset email sent (simulated).')
        else:
            messages.error(request, 'Email not found.')
    return render(request, 'password_reset.html')

@login_required
def edit_profile(request):
    profile = PatientProfile.objects.get(user=request.user)
    current_user = request.user


    if request.method == 'POST':
        form = PatientProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')  # Redirect to a profile detail view
    else:
        form = PatientProfileForm(instance=profile)
        context = {
            'profile': profile,
            'current_user': current_user,
            'form': form,

        }
    return render(request, 'edit_profile.html', context)

@login_required
def profile_detail(request):
    profile = PatientProfile.objects.get(user=request.user)
    current_user = request.user
    context = {
        'profile': profile,
        'current_user': current_user

    }

    return render(request, 'profile_detail.html', context)
