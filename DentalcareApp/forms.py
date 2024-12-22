
from .models import ImageModel,Appointment,PatientProfile
from django import forms


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'title', 'price']

    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter image title'}))
    price = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter image price'}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))


class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['date_of_birth', 'phone_number', 'address', 'medical_history', 'dental_records', 'xray_image']



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'