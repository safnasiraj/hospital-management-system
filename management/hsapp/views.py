from django.shortcuts import render, redirect
from .models import DoctorProfile,PatientProfile
from .forms import DoctorProfileForm, PatientProfileForm



# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def doctor_landing(request):
    return render(request, 'doctor/doctor_landing.html') 

def doctor_login(request):
    return render(request,'doctor/doctor_login.html')

def doctor_login_check(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        profile = DoctorProfile.objects.filter(username=username, password=password)
        if profile:
            for i in profile:
                if i.status=="active":
                    user_details=DoctorProfile.objects.get(username=username, password=password)
                    id = user_details.id
                    name = user_details.name

                    request.session['id'] = id
                    request.session['name'] = name
                    
                    return redirect('doctor_welcome')

            else:
                return render(request,'doctor/doctor_authentication_failure.html')

            
        else:
            return render(request,'doctor/doctor_authentication_failure.html')
    else:
        return render(request,'doctor/doctor_authentication_failure.html')

def doctor_authentication_failure(request):
    return render(request,'doctor/doctor_authentication_failure.html')

def doctor_welcome(request):
    id = request.session['id']
    name = request.session['name']
    return render(request,"doctor/doctor_welcome.html",{'id':id, 'name':name})

def doctor_register(request):
    form =  DoctorProfileForm()
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'doctor/doctor_registration_success.html')

    return render(request, 'doctor/doctor_register.html',{'form': form})

def doctor_registration_success(request):
    return render(request, 'doctor/doctor_registration_success.html') 

def doctor_update(request):
    doctor_id = request.session.get('id')
    if not doctor_id:
        return redirect('doctor_login')

    doctor = DoctorProfile.objects.get(id=doctor_id)
    form = DoctorProfileForm(instance=doctor)

    if request.method == "POST":
        form = DoctorProfileForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("doctor_welcome")

    return render(request, 'doctor/doctor_update.html', {'form': form})

def doctor_delete(request):
    return render(request, 'doctor/doctor_delete.html') 

def doctor_delete_confirm(request):

    doctor_id = request.session.get('id')
    
    if doctor_id:
        try:
            doctor = DoctorProfile.objects.get(id=doctor_id)
            doctor.delete()
            request.session.flush()  # Clear session after deletion
            return render(request, 'doctor/doctor_deleted_success.html')
        except DoctorProfile.DoesNotExist:
            return redirect('doctor_login')
    else:
        return redirect('doctor_login')
    
def patient_landing(request):
    return render(request, 'patient/patient_landing.html') 

def patient_login(request):
    return render(request,'patient/patient_login.html')

def patient_login_check(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        profile = PatientProfile.objects.filter(username=username, password=password)
        if profile:
            user_details=PatientProfile.objects.get(username=username, password=password)
            id = user_details.id
            name = user_details.name

            request.session['id'] = id
            request.session['name'] = name
            
            return redirect('patient_welcome')
            
        else:
            return render(request,'patient/patient_authentication_failure.html')
    else:
        return render(request,'patient/patient_authentication_failure.html')
    
def patient_authentication_failure(request):
    return render(request,'patient/patient_authentication_failure.html')

def patient_welcome(request):
    id = request.session['id']
    name = request.session['name']
    return render(request,"patient/patient_welcome.html",{'id':id, 'name':name})

def patient_register(request):
    form =  PatientProfileForm()
    if request.method == 'POST':
        form = PatientProfileForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'patient/patient_registration_success.html')

    return render(request, 'patient/patient_register.html',{'form': form})

def patient_registration_success(request):
    return render(request, 'patient/patient_registration_success.html') 

def patient_update(request):
    patient_id = request.session.get('id')
    if not patient_id:
        return redirect('patient_login')

    patient = PatientProfile.objects.get(id=patient_id)
    form = PatientProfileForm(instance=patient)

    if request.method == "POST":
        form = PatientProfileForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return redirect("patient_welcome")

    return render(request, 'patient/patient_update.html', {'form': form})

def patient_delete(request):
    return render(request, 'patient/patient_delete.html') 

def patient_delete_confirm(request):

    patient_id = request.session.get('id')
    
    if patient_id:
        try:
            patient = PatientProfile.objects.get(id=patient_id)
            patient.delete()
            request.session.flush()  # Clear session after deletion
            return render(request, 'patient/patient_deleted_success.html')
        except PatientProfile.DoesNotExist:
            return redirect('patient_login')
    else:
        return redirect('patient_login')
    

def patients_view(request):
    did=request.session['id']
    patients = PatientProfile.objects.filter(doctor_id=did)
    return render(request, 'doctor/patients_view.html', {'patients': patients})


def doctors_view(request):
    doctors = DoctorProfile.objects.all()
    return render(request, 'patient/doctors_view.html', {'doctors': doctors})