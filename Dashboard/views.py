from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import	authenticate,	login,	logout
from django.contrib import messages
from django.contrib.auth.decorators	import login_required
from .sys import sys
from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.
class dashboard_login(LoginView):
    template_name = 'Dashboard/login.html'
    redirect_authenticated_user = True
# def dashboard_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username,password=password)
#         if user is not  None :
#             login(request, user)
#             context = {
#                 "sysinfo": sys(),
#                 "user_last_login": request.user.last_login,
#             }
#             return render_to_response('Dashboard/index.html', context)
#         else :
#             messages.error(request, 'Invaild login !')
#             return render(request, 'Dashboard/login.html')
#     elif  request.user.is_authenticated:
#         context = {
#             "sysinfo": sys(),
#             "user_last_login": request.user.last_login,
#         }
#         return render_to_response('Dashboard/index.html', context )
#     else:
#         return render(request, 'Dashboard/login.html')

class dashboard_logout(LogoutView):
     template_name = 'Dashboard/login.html'
     next_page = '/dashboard/login'
# def dashboard_logout(request):
#     logout(request)
#     messages.success(request, 'logout success')
#     return redirect('/dashboard/')

@login_required
def dashboard_index(request):
    if request.user.is_authenticated :
        context = {
            "sysinfo": sys(),
            "user_last_login": request.user.last_login,
        }
        return render_to_response('Dashboard/index.html', context)
    else:
        return redirect('Dashboard:login')
