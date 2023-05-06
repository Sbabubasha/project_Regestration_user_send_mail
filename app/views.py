from django.shortcuts import render
from  django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
from app.forms import *
def register(request):
    ufo=Userforms()
    pfo=Profileforms()
    d={'ufo':ufo,'pfo':pfo}

    
    if request.method=='POST' and request.FILES:
        UOD=Userforms(request.POST)
        POD=Profileforms(request.POST,request.FILES)
        if UOD.is_valid() and POD.is_valid():
            NUOD=UOD.save(commit=False)
            NUOD.set_password(UOD.cleaned_data['password'])
            NUOD.save()

            NPOD=POD.save(commit=False)
            NPOD.username=NUOD
            NPOD.save()

            #send_mail('subject','message/content of mail','from mail id', recipient_list',fail_silent=True)
            send_mail('Rigistraion is done successfully..!',
                      "iam a developer at jspyders we are hiring if you want to intrested join our company",
                      'npersonal47@gmail.com',
                      [NUOD.email],
                      fail_silently=True )




            return HttpResponse('registraion is done...!')
        else:
            return HttpResponse('invalid data..!')
    
    return render(request,'register.html',d)