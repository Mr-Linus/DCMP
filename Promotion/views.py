from django.shortcuts import render,redirect,reverse
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from django.conf  import settings
# Create your views here.

# Tags: 重新使用ModelForm重写代码,以求得精简,准确,高效以及更精准的编码规范.
def index(request):
    if request.method == 'POST':
       form = ContactForm(request.POST)
       if form.is_valid():
           form.save()
           if send_mail('From: DCMP ',
                        'Dear '+form.cleaned_data['name']+": \n"+'    We have received your Message :'+form.cleaned_data['text'],
                        settings.DEFAULT_FROM_EMAIL,
                        form.cleaned_data['email'].split(),fail_silently=True,) == 1:
               messages.success(request, "Message Send Successfully !!")
           else:
               messages.error(request, 'Send Error!')
       else:
            if not form.name:
               messages.error(request,'Name	is	required!!')
            if not form.email:
                messages.error(request,'Email	is	required!!')
            if not form.text:
                messages.error(request,'Message is	required!!')
       return redirect(reverse('Promotion:index')+'#contact-section')
    else:
        form = ContactForm({'name':'Your Name','email':'example@test.com','text':'Leave us a Message.'})
        return render(request,'Promotion/index.html',{"form":form})






