from django.shortcuts import redirect,render_to_response,render
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth import	authenticate,	login,	logout
#from django.contrib import messages
#from django.contrib.auth.decorators	import login_required
from .sys import sys,sys_update
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.base import TemplateView
import docker
from time import sleep
from django.views.generic.base import RedirectView
# Create your views here.
class dashboard_login_view(LoginView):
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

class dashboard_logout_view(LogoutView):
     template_name = 'Dashboard/login.html'
     next_page = '/dashboard/login'
# def dashboard_logout(request):
#     logout(request)
#     messages.success(request, 'logout success')
#     return redirect('/dashboard/')
# def dashboard_index(request):
#     if request.user.is_authenticated :
#         context = {
#             "sysinfo": sys(),
#             "user_last_login": request.user.last_login,
#         }
#         return render_to_response('Dashboard/index.html', context)
#     else:
#         return redirect('Dashboard:login')

class dashboard_index_view(TemplateView):
    template_name = 'Dashboard/index.html'

    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs)
        context['sysinfo'] = sys()
        context['con_run'] = docker.from_env().info()['ContainersRunning']
        context['con_stop'] = docker.from_env().info()['ContainersStopped']
        context['con_pause'] = docker.from_env().info()['ContainersPaused']
        context['user_last_login'] = self.request.user.last_login
        context['user'] = self.request.user.username
        return context
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        else:
            return redirect('/dashboard/login')


@csrf_exempt
def dashobard_containers_view(request):
    template_name = 'Dashboard/containers.html'
    if request.user.is_authenticated:
        if request.method == "POST":
            con_name = request.POST.getlist("con_name")
            if 'start' in request.POST:
                for con in con_name:
                    sys().client.containers.get(con).start()
            elif 'stop'in request.POST:
                for con in con_name:
                    sys().client.containers.get(con).stop()
            elif 'restart' in request.POST:
                for con in con_name:
                    sys().client.containers.get(con).restart()
            elif 'remove'in request.POST:
                for con in con_name:
                    sys().client.containers.get(con).remove()
            context = {
                "con_list": docker.from_env().containers.list(all=True),
                "user_last_login": request.user.last_login,
                "user": request.user.username,
            }
            sleep(3)
            return render_to_response(template_name,context)
        if request.method == "GET":
            context = {
                "con_list": docker.from_env().containers.list(all=True),
                "user_last_login": request.user.last_login,
                "user": request.user.username,
            }
            return render_to_response(template_name, context)
    else:
        return redirect('/dashboard/login')






    # def get_context_data(self, **kwargs,):
    #     context = super().get_context_data(**kwargs)
    #     context['sysinfo'] = sys()
    #     context['user_last_login'] = self.request.user.last_login
    #     context['user'] = self.request.user.username
    #     return context
    # def get(self, request, *args, **kwargs):
    #         context = self.get_context_data(**kwargs)
    #         return self.render_to_response(context)

    # def post(request):
    #     if request.user.is_authenticated:
    #         if request.POST.has_key('start'):
    #             for con in con_id:
    #                 sys().client.containers.get(container_id=con).start()
    #         elif request.POST.has_key('stop'):
    #             for con in con_id:
    #                 sys().client.containers.get(container_id=con).stop()
    #         elif request.POST.has_key('restart'):
    #             for con in con_id:
    #                 sys().client.containers.get(container_id=con).restart()
    #         elif request.POST.has_key('remove'):
    #             for con in con_id:
    #                 sys().client.containers.get(container_id=con).remove()
    #         else:
    #             return redirect('/dashboard/login')
    #         return self.render_to_response(context)
    #     else:
    #         return redirect('/dashboard/login')

