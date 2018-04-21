from django.shortcuts import render,reverse,redirect,HttpResponseRedirect,render_to_response
from django.contrib.auth	import	authenticate,	login,	logout
from django.contrib import messages
from django.contrib.auth.decorators	import	login_required
from django.template import Context
from  .sys import sys
# Create your views here.
def dashboard_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not  None :
            messages.success(request, 'login Success!')
            login(request,user)
            sysinfo = sys()
            context = {
                "sysinfo": sysinfo,
            }
            return render_to_response('Dashboard/index.html', context)
        else :
            messages.error(request, 'Invaild login !')
            return render(request, 'Dashboard/login.html')
    elif  request.user.is_authenticated:
        messages.success(request, 'login Success!')
        sysinfo = sys()
        context = {
            "sysinfo": sysinfo,
        }
        return render_to_response('Dashboard/index.html', context)
    else:
        return render(request, 'Dashboard/login.html')

def dashboard_logout(request):
    logout(request)
    messages.success(request, 'logout success')
    return redirect('/dashboard/')

@login_required
def dashboard_index(request):
    if request.user.is_authenticated :
        sysinfo = sys()
        context = {
            "sysinfo": sysinfo,
        }
        return render_to_response( 'Dashboard/index.html', context)
    else:
        return  redirect('Dashboard:login')
