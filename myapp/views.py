from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from myapp.models import Appointment,Doctor
from django.contrib.auth.decorators import login_required


# Create your views here.
def About(request):
    return render(request,'about.html')

def Home(request):
    return render(request,'home.html')

def Contact(request):
    return render(request,'contact.html')

def DoctorAvailability(request):
    Doctors = Doctor.objects.all()
    print(Doctors)
    context = {'Doctors': Doctors}
    return render(request, 'doctoravailability.html', context)

@login_required
def patient_appoint(request):
    doctors = Doctor.objects.all() 
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        symptoms = request.POST['symptoms']
        mobile = request.POST['mobile']
        address = request.POST['address']
        date = request.POST['date']
        time = request.POST['time']
        doctor_id = request.POST['doctor']
        doctor = Doctor.objects.get(pk=doctor_id) 

        appointment = Appointment(name=name, age=age, gender=gender, symptoms= symptoms, mobile=mobile, address=address, date=date, time=time,doctor=doctor)
        appointment.save()
        return redirect('sucess')
        return redirect('home')

    return render(request, 'appointment.html',{'doctors': doctors})    
  
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout



def index(request):
    appointments = Appointment.objects.all()
    print(appointments)
    context = {'appointments': appointments}
    return render(request, 'index.html', context)

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login_user')
    return render(request, 'register.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']  # Corrected this line

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Corrected this line
            return redirect('index')
        else:
            return render(request, 'login.html')    

    return render(request, 'login.html')

def logout_user(request):
    logout(request)  
    return redirect('home')  # Corrected this line

def sucess(request):
    return render(request,'sucess.html')

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

def email_form(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('email', '')

        # Send the email to the provided email address
        send_mail(subject, message, from_email, [from_email])
        return redirect('home')

    return render(request, 'email_form.html')    