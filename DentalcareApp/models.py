from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    doctor = models.CharField(max_length=100)
    message = models.TextField()
    appointment_time = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    contact_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Member(models.Model):
    profile = models.ImageField(upload_to='profile-images/')
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # Link to the user model
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)  # Medical history notes
    dental_records = models.TextField(blank=True, null=True)  # Detailed dental records
    xray_image = models.ImageField(upload_to='xray_images/', blank=True, null=True)  # Store X-ray images
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update timestamp
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_contact_info(self):
        return f"{self.phone_number}, {self.address}"
