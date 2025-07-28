from django.urls import path
from django.contrib import admin

from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('doctor/landing/', views.doctor_landing, name='doctor_landing'),
    path('doctor/login/', views.doctor_login, name='doctor_login'),
    path('doctor/register/', views.doctor_register, name='doctor_register'),
    path('doctor/login_check/', views.doctor_login_check, name='doctor_login_check'),
    path('doctor/authentication_failure/', views.doctor_authentication_failure, name='doctor_authentication_failure'),
    path('doctor/welcome/', views.doctor_welcome, name='doctor_welcome'),
    path('doctor/update/', views.doctor_update, name='doctor_update'),
    path('doctor/delete/', views.doctor_delete, name='doctor_delete'),
    path('doctor/delete_confirm/', views.doctor_delete_confirm, name='doctor_delete_confirm'),
    path('patient/landing/', views.patient_landing, name='patient_landing'),
    path('patient/login/', views.patient_login, name='patient_login'),
    path('patient/register/', views.patient_register, name='patient_register'),
    path('patient/login_check/', views.patient_login_check, name='patient_login_check'),
    path('patient/authentication_failure/', views.patient_authentication_failure, name='patient_authentication_failure'),
    path('patient/welcome/', views.patient_welcome, name='patient_welcome'),
    path('patient/update/', views.patient_update, name='patient_update'),
    path('patient/delete/', views.patient_delete, name='patient_delete'),
    path('patient/delete_confirm/', views.patient_delete_confirm, name='patient_delete_confirm'),
    path('doctor/patients_view/', views.patients_view, name='patients_view'),
    path('patient/octors_view/', views.doctors_view, name='doctors_view'),
    path('admin/', admin.site.urls),
]