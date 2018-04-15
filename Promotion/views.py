from django.shortcuts import render,redirect,reverse
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact
# Create your views here.
DEFAULT_FROM_EMAIL = 'DCMP <mrfunky@gmx.com>'

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email', '')
        text = request.POST.get('text','')
        if not name:
            messages.error(request,'Name	is	required!!')
        if not email:
            messages.error(request,'Email	is	required!!')
        if not text:
            messages.error(request,'Text is	required!!')
        elif send_mail('From:'+name,text,'You are already send :'+DEFAULT_FROM_EMAIL,email.split(),fail_silently=True,) == 1:
            Contact.objects.update_or_create(name=name,email=email,text=text)
            messages.success(request, "Message Send Successfully !!")
        else:
            messages.error(request, 'Send Error!')
        return redirect(reverse('Promotion:index')+'#contact-section')
    return render(request,'Promotion/index.html')






