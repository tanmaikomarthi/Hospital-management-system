from django.urls import path
from myapp.views import email_form,sucess,About,Home,Contact,DoctorAvailability,patient_appoint,index,registration,login_user,logout_user

urlpatterns = [
    path('',Home,name='home'),
    path('about/',About,name='about'),
    path('contact/',Contact,name='contact'),
    path('doctoravailability/',DoctorAvailability,name='doctoravailability'),
    path('appointment/',patient_appoint,name='patient_appoint'),
    path('index/', index, name='index'),
    path('registration/', registration, name='registration'),
    path('login_user/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'), 
    path('sucess/',sucess,name='sucess'),
    path('email/', email_form, name='email_form'),
]
