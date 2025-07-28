from django import forms

from .models import DoctorProfile, PatientProfile

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = '__all__'

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = '__all__'
