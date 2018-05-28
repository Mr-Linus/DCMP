from django.shortcuts import redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth import	authenticate,	login,	logout
#from django.contrib import messages
#from django.contrib.auth.decorators	import login_required
from Dashboard.sys import sys,sys_swarm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.contrib.auth import logout
import docker
from  Dashboard.form import DeployForm, PullForm, CreateVolumeForm,CreateNetworkForm, ChangePasswordForm,UserCreationForm
# from django.views.generic.base import RedirectView
import datetime
from Dashboard.models import User
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sysinfo'] = sys()
        context['con_run'] = docker.from_env().info()['ContainersRunning']
        context['con_stop'] = docker.from_env().info()['ContainersStopped']
        context['con_pause'] = docker.from_env().info()['ContainersPaused']
        context['user_last_login'] = self.request.user.last_login
        context['user'] = self.request.user.username
        context['con_num'] = len(docker.from_env().containers.list(all=True))
        return context
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.dashboard_permission:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        else:
            return redirect('/dashboard/login')


@csrf_exempt
def dashobard_containers_view(request):
    template_name = 'Dashboard/containers.html'
    if request.user.is_authenticated and request.user.containers_permission:
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

@csrf_exempt
def dashboard_deploy_view(request):
    template_name = 'Dashboard/deploy.html'
    if request.user.is_authenticated and request.user.containers_permission:
        if request.method == "POST":
            form = DeployForm(request.POST)
            if form.is_valid():
                sys().client.containers.run(
                    image=form.cleaned_data['image'],
                    command=form.cleaned_data['cmd'],
                    auto_remove=form.cleaned_data['auto_remove'],
                    tty=form.cleaned_data['tty'],
                    ports=form.cleaned_data['ports'],
                    working_dir=form.cleaned_data['work_dir'],
                    name=form.cleaned_data['name']
                )
                return redirect('/dashboard/containers')
        if request.method == "GET":
            form = DeployForm()
            return render_to_response(template_name, context={'form': form, 'user':request.user.username, 'user_last_login':request.user.last_login})
    else:
        return redirect('/dashboard/login')

@csrf_exempt
def dashobard_swarm_view(request):
    template_name = 'Dashboard/swarm.html'
    context = {
        "swarm": sys_swarm(),
        "user_last_login": request.user.last_login,
        "user": request.user.username,
    }
    if request.user.is_authenticated and request.user.swarm_permission:
        if request.method == "GET":
            return render_to_response(template_name, context)
        if request.method == "POST":
            if 'reload' in request.POST:
                sys_swarm().reload()
            elif 'update' in request.POST:
                sys_swarm().update()

            return render_to_response(template_name, context)
    else:
        return redirect('/dashboard/login')

@csrf_exempt
def dashobard_images_view(request):
    template_name = 'Dashboard/images.html'
    con_image_list = []
    for con in docker.from_env().containers.list(all=True):
        con_image_list += con.image.tags
    context = {
        "images": docker.from_env().images.list(all=True),
        "user_last_login": request.user.last_login,
        "user": request.user.username,
        "con_image_list": con_image_list,
        "form":PullForm(),
    }
    if request.user.is_authenticated and request.user.images_permission:
        if request.method == "GET":
            return render_to_response(template_name, context)
        if request.method == "POST":
            if 'remove' in request.POST:
                image_tags = request.POST.getlist('image')
                for image_tag in image_tags:
                    sys().image.remove(image_tag)
            if 'pull' in request.POST:
                pull_form = PullForm(request.POST)
                if pull_form.is_valid():
                    sys().image.pull(pull_form.cleaned_data['pull_image'])
        return redirect('/dashboard/index')
    else:
        return redirect('/dashboard/login')

@csrf_exempt
def dashboard_volume_view(request):
    template_name = 'Dashboard/volumes.html'
    context = {
        "user_last_login": request.user.last_login,
        "user": request.user.username,
        "volumes": sys().client.volumes.list(),
        "form": CreateVolumeForm(),
    }
    if request.user.is_authenticated and request.user.volumes_permission:
        if request.method == "GET":
            return render_to_response(template_name, context)
        if request.method == "POST":
            if 'remove' in request.POST:
                volume_names = request.POST.getlist('volume_name')
                for volume_name in volume_names:
                    sys().client.volumes.get(volume_name).remove()
            if 'create' in request.POST:
                create_form = CreateVolumeForm(request.POST)
                if create_form.is_valid():
                    sys.client.volumes.create(
                        name=create_form.cleaned_data['name'],
                        driver=create_form.cleaned_data['driver']
                    )
        return redirect('/dashboard/index')
    else:
        return redirect('/dashboard/login')


@csrf_exempt
def dashboard_network_view(request):
    template_name = 'Dashboard/networks.html'
    context = {
        "user_last_login": request.user.last_login,
        "user": request.user.username,
        "form": CreateNetworkForm(),
        "networks": docker.from_env().networks.list()
    }
    if request.user.is_authenticated & request.user.networks_permission:
        if request.method == "GET":
            return render_to_response(template_name, context)
        if request.method == "POST":
            if 'remove' in request.POST:
                network_ids = request.POST.getlist('network_id')
                for network_id in network_ids:
                    sys().client.networks.get(network_id).remove()
            if 'create' in request.POST:
                create_form = CreateNetworkForm(request.POST)
                if create_form.is_valid():
                    sys.client.networks.create(
                        name=create_form.cleaned_data['name'],
                        driver=create_form.cleaned_data['driver']
                    )
        return redirect('/dashboard/index')
    else:
        return redirect('/dashboard/login')


class dashboard_events_view(TemplateView):
    template_name = 'Dashboard/events.html'
    permission_required = 'events_permission'
    def get_events_list(self):
        event_list=[]
        count=0
        for event in docker.from_env().events(decode=True,since=(datetime.datetime.now() - datetime.timedelta(days=5)),until=datetime.datetime.now()):
            event_list.append(event)
            count += 1
            if count == 20:
                break
        return event_list
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_last_login'] = self.request.user.last_login
        context['user'] = self.request.user.username
        context['events_list'] = self.get_events_list()
        return context
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated & request.user.events_permission:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        else:
            return redirect('/dashboard/login')

@csrf_exempt
def dashboard_settings_view(request):
    template_name = 'Dashboard/settings.html'
    user_perm = request.user
    if request.user.is_authenticated:
        context = {
            "user_last_login": request.user.last_login,
            "user": request.user.username,
            "user_info": user_perm,
            "dashboard": user_perm.dashboard_permission,
            "containers": user_perm.containers_permission,
            "images": user_perm.images_permission,
            "swarm": user_perm.swarm_permission,
            "volumes": user_perm.volumes_permission,
            "events": user_perm.events_permission,
            "networks": user_perm.networks_permission,
            "chpasswd_form": ChangePasswordForm(),
        }
        if request.method == "GET":
            return render_to_response(template_name, context)
        if request.method == "POST":
            if 'change' in request.POST:
                password_form = ChangePasswordForm(request.POST)
                if password_form.is_valid():
                    if password_form.cleaned_data['confirm'] == password_form.cleaned_data['password']:
                        request.user.set_password(
                            password_form.cleaned_data['password'],
                        )
                        request.user.save()
                        # logout(request)
                        redirect('/dashboard/login')
        return redirect('/dashboard/index')
    else:
        return redirect('/dashboard/login')


@csrf_exempt
def dashboard_add_update_view(request):
    template_name = 'Dashboard/add_update.html'
    if request.user.is_authenticated and request.user.is_superuser:
        context = {
            "user_last_login": request.user.last_login,
            "user": request.user.username,
            "add_update_form": UserCreationForm(),
        }
        if request.method == "GET":
            return render_to_response(template_name, context)
        if request.method == "POST":
                add_update_form = UserCreationForm(request.POST)
                if add_update_form.is_valid():
                       if add_update_form.confirm_password():
                            add_update_form.save(commit=True)
        return redirect('/dashboard/index')
    else:
        return redirect('/dashboard/login')

