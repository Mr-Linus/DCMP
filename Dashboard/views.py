from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import resolve_url
from Dashboard.sys import sys, sys_swarm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView, View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import time


from django.conf import settings
import docker
from Dashboard.form import DeployForm, PullForm, CreateVolumeForm, \
    CreateNetworkForm, ChangePasswordForm, UserCreationForm

import datetime
from Dashboard.tasks import deploy, image_pull

# Create your views here.


class dashboard_login_view(LoginView):
    template_name = 'Dashboard/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        url = self.get_redirect_url()
        messages.add_message(self.request, messages.SUCCESS,
                             "Welcome to DCMP Dashboard - A beautiful Docker Container Management Platform.")
        return url or resolve_url(settings.LOGIN_REDIRECT_URL)


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


class dashboard_index_view(LoginRequiredMixin, TemplateView):
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
            return self.render_to_response(context=context)
        else:
            return redirect('/dashboard/login')


class ContainersView(LoginRequiredMixin, TemplateView):
    template_name = 'Dashboard/containers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = docker.from_env().containers.list(all=True)
        context["user_last_login"] = self.request.user.last_login
        context["user"] = self.request.user.username
        return context

    def get(self, request, *args, **kwargs):
        if request.user.containers_permission:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context=context)
        else:
            return redirect('/dashboard/login')

    def post(self, request, *args, **kwargs):
        con_name = request.POST.getlist("con_name")
        if request.user.containers_permission:
            if 'start' in request.POST:
                for con in con_name:
                    try:
                        sys().client.containers.get(con).start()
                        messages.add_message(request, messages.SUCCESS, "Contianer: "+str(con)+" start Success")
                    except:
                        messages.add_message(request, messages.ERROR, "Contianer: "+str(con)+"  start Failed")
            elif 'stop'in request.POST:
                for con in con_name:
                    try:
                        sys().client.containers.get(con).stop()
                        messages.add_message(request, messages.WARNING, "Contianer: " + str(con) + " stop Success")
                    except:
                        messages.add_message(request, messages.ERROR, "Contianer: " + str(con) + "  stop Failed")
            elif 'restart' in request.POST:
                for con in con_name:
                    try:
                        sys().client.containers.get(con).restart()
                        messages.add_message(request, messages.SUCCESS, "Contianer: " + str(con) + " restart Success")
                    except:
                        messages.add_message(request, messages.ERROR, "Contianer: " + str(con) + "  restart Failed")
            elif 'remove'in request.POST:
                for con in con_name:
                    try:
                        sys().client.containers.get(con).stop()
                        sys().client.containers.get(con).remove()
                        messages.add_message(request, messages.SUCCESS, "Contianer: " + str(con) + " remove Success")
                    except:
                        messages.add_message(request, messages.ERROR, "Contianer: " + str(con) + "  remove Failed")
            context = {
                "object_list": docker.from_env().containers.list(all=True),
                "user_last_login": request.user.last_login,
                "user": request.user.username,
            }
            return render(self.request, template_name=self.template_name, context=context)
        return redirect('/dashboard/login')



@csrf_exempt
def dashboard_deploy_view(request):
    template_name = 'Dashboard/deploy.html'
    if request.user.is_authenticated and request.user.containers_permission:
        if request.method == "POST":
            form = DeployForm(request.POST)
            if form.is_valid():
                deploy.delay(
                    image=form.cleaned_data['image'],
                    command=form.cleaned_data['cmd'],
                    auto_remove=form.cleaned_data['auto_remove'],
                    tty=form.cleaned_data['tty'],
                    ports=form.cleaned_data['ports'],
                    volumes=form.cleaned_data['volumes'],
                    name=form.cleaned_data['name'],
                    hostname=form.cleaned_data['hostname'],
                    cpu=form.cleaned_data['cpu'],
                    mem=form.cleaned_data['mem'],
                    privileged=form.cleaned_data['privileged'],
                    network=form.cleaned_data['network'],
                )
                messages.add_message(request, messages.INFO, 'Deloying the Container. Please wait and refresh the page after a while. ')
                time.sleep(3)
                return redirect('/dashboard/containers')
        if request.method == "GET":
            form = DeployForm()
            return render(request,
                          template_name=template_name,
                          context={'form': form,
                                   'user':request.user.username,
                                   'user_last_login':request.user.last_login
                                   }
                          )
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
            return render(request, template_name=template_name, context=context)
        if request.method == "POST":
            if 'reload' in request.POST:
                try:
                    sys_swarm().reload()
                    messages.add_message(request, messages.SUCCESS, 'Reloading the Swarm.')
                except:
                    messages.add_message(request, messages.ERROR, 'Reloading the Swarm Error.')
            elif 'update' in request.POST:
                try:
                    sys_swarm().update()
                    messages.add_message(request, messages.SUCCESS, 'Updating the Swarm.')
                except:
                    messages.add_message(request, messages.ERROR, 'Updating the Swarm Error.')
            return render(request, template_name=template_name, context=context)
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
        "form": PullForm(),
    }
    if request.user.is_authenticated and request.user.images_permission:
        if request.method == "GET":
            return render(request, template_name=template_name, context=context)
        if request.method == "POST":
            if 'remove' in request.POST:
                try:
                    image_tags = request.POST.getlist('image')
                    for image_tag in image_tags:
                        sys().image.remove(image_tag)
                    messages.add_message(request,
                                         messages.SUCCESS,
                                         'Removing images..Please wait.'
                                         )
                except:
                    messages.add_message(request,
                                         messages.WARNING,
                                         'Removing images failed.'
                                         )
            if 'pull' in request.POST:
                pull_form = PullForm(request.POST)
                if pull_form.is_valid():
                    try:
                        image_pull.delay(pull_form.cleaned_data['pull_image'])
                        messages.add_message(request,
                                             messages.SUCCESS,
                                             'Pulling images.Please wait and refresh the page after a while.'
                                             )
                    except:
                        messages.add_message(request,
                                             messages.WARNING,
                                             'Pulling images failed.'
                                             )
        return redirect('/dashboard/images')
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
            return render(request, template_name=template_name, context=context)
        if request.method == "POST":
            if 'remove' in request.POST:
                volume_names = request.POST.getlist('volume_name')
                for volume_name in volume_names:
                    try:
                        sys().client.volumes.get(volume_name).remove()
                        messages.add_message(request, messages.SUCCESS,
                                             'Removing volumes:'+volume_name+'.Please wait and refresh the page after a while.'
                                             )
                    except:
                        messages.add_message(request, messages.WARNING,
                                             'Removing volumes:'+volume_name+' Error'
                                             )

            if 'create' in request.POST:
                create_form = CreateVolumeForm(request.POST)
                if create_form.is_valid():
                    try:
                        sys.client.volumes.create(
                            name=create_form.cleaned_data['name'],
                            driver=create_form.cleaned_data['driver']
                        )
                        messages.add_message(request, messages.SUCCESS,
                                             'Creating volumes:'+create_form.cleaned_data['name']+'.Please wait and refresh the page after a while.'
                                             )
                    except:
                        messages.add_message(request, messages.WARNING,
                                             'Creating volumes:'+create_form.cleaned_data['name']+' Error'
                                             )
        return redirect('/dashboard/volumes')
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
            return render(request, template_name=template_name, context=context)
        if request.method == "POST":
            if 'remove' in request.POST:
                network_ids = request.POST.getlist('network_id')
                for network_id in network_ids:
                    try:
                        sys().client.networks.get(network_id).remove()
                        messages.add_message(request, messages.SUCCESS,
                                             'Removing networks:'+network_id+'.Please wait and refresh the page after a while.'
                                             )
                    except:
                        messages.add_message(request, messages.WARNING, 'Removing networks:'+network_id+' Error')

            if 'create' in request.POST:
                create_form = CreateNetworkForm(request.POST)
                if create_form.is_valid():
                    try:
                        sys.client.networks.create(
                            name=create_form.cleaned_data['name'],
                            driver=create_form.cleaned_data['driver'],
                            scope=create_form.cleaned_data['scope']
                        )
                        messages.add_message(request, messages.SUCCESS,
                                             'Creating networks:' +create_form.cleaned_data['name']+ '.Please wait and refresh the page after a while.'
                                             )
                    except:
                        messages.add_message(request, messages.WARNING,
                                             'Creating networks:' + create_form.cleaned_data['name'] + ' Error'
                                             )
        return redirect('/dashboard/networks')
    else:
        return redirect('/dashboard/login')


class dashboard_events_view(LoginRequiredMixin, TemplateView):
    template_name = 'Dashboard/events.html'
    permission_required = 'events_permission'

    def get_events_list(self):
        event_list=[]
        count = 0
        for event in docker.from_env().events(decode=True,
                                              since=(datetime.datetime.now() - datetime.timedelta(days=5)),
                                              until=datetime.datetime.now()):
            event_list.append(event)
            count += 1
            if count == 5:
                break
        return event_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_last_login'] = self.request.user.last_login
        context['user'] = self.request.user.username
        context['events_list'] = self.get_events_list()
        return context

    def get(self, request, *args, **kwargs):
        if request.user.events_permission:
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
            return render(request, template_name=template_name, context=context)
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
            return render(request, template_name=template_name, context=context)
        if request.method == "POST":
                add_update_form = UserCreationForm(request.POST)
                if add_update_form.is_valid():
                    if add_update_form.confirm_password():
                        add_update_form.save(commit=True)
        return redirect('/dashboard/index')
    else:
        return redirect('/dashboard/login')


class DetailView(LoginRequiredMixin, TemplateView):
    template_name = 'Dashboard/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_last_login'] = self.request.user.last_login
        context['user'] = self.request.user.username
        context['con'] = docker.from_env().containers.get(self.request.path.split('containers/')[1])
        return context

    def get(self, request, *args, **kwargs):
        if request.user.events_permission:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context=context)
        else:
            return redirect('/dashboard/login')


class Update_ConNumView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(sys().con_num)


class Update_CPUPerView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(str(sys().cpu_percent())+"%")


class Update_MemPerView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(str(sys().mem_persent)+"%")
