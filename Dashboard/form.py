from django import forms
from Dashboard.models import User
class DeployForm(forms.Form):
    name = forms.CharField(max_length=100,
                           label='Contianer Name',
                           help_text="Please input the Container name.This is a custom option",
                           required=False
                           )
    image = forms.CharField(max_length=100,
                            label='Image',
                            help_text="This is a required option",
                            required=True
                            )
    auto_remove = forms.BooleanField(
        help_text="Automatically close the container when a problem occurs",
        label="Auto remove",
        required=False
    )
    privileged =forms.BooleanField(
        help_text="Give extended privileges to this container.",
        label="Privileged",
        required=False
    )
    cpu = forms.CharField(
        max_length=7,
        label='CPU Shares',
        help_text="CPU shares (relative weight). default:1024",
        required=False
    )
    mem = forms.CharField(
        max_length=7,
        label='Memory',
        help_text="Memory limit. Accepts float values (which represent the memory limit of the created container in bytes) or a string with a units identification char (100000b, 1000k, 128m, 1g).",
        required=False
    )
    hostname = forms.CharField(
                                max_length=100,
                                label='Contianer Hostname',
                                help_text="Please input the Container HostName.This is a custom option",
                                required=False
    )
    ports = forms.CharField(max_length=100,
                            label='Ports',
                            help_text="Export Posts .For example, {'2222/tcp': 3333} will expose port 2222 inside the container as port 3333 on the host.",
                            required=False
                            )
    tty = forms.BooleanField(help_text='Allocate a pseudo-TTY.',
                             label='tty',
                             required=False
                             )
    network = forms.CharField(
                            max_length=100,
                            label='Network',
                            help_text='Name of the network this container will be connected to at creation time.',
                            required=False
    )
    volumes = forms.CharField(max_length=100,
                               label="Volumes",
                               help_text="A dictionary to configure volumes mounted inside the container. For exapmle,{'/home/user1/': {'bind': '/mnt/vol2', 'mode': 'rw'},'/var/www': {'bind': '/mnt/vol1', 'mode': 'ro'}}",
                               required=False
                               )
    cmd = forms.CharField(max_length=100,
                          label='Command',
                          help_text="The command to run in the container.",
                          required=False
                          )


class PullForm(forms.Form):
    pull_image = forms.CharField(
        max_length=20,
        label="Image Name (e.g. ubuntu:14.04)",
        help_text="Note: if you don't specify the tag in the image name, latest will be used.",
        label_suffix="Image Name e.g. ubuntu:14.04",
        required=True,)


class CreateVolumeForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        label='Name',
        help_text="Volume Name",
        required=True
    )
    driver = forms.CharField(
        max_length=30,
        label='Driver',
        help_text='Driver configuration',
        required=False
    )


class CreateNetworkForm(forms.Form):
    SCOPE_CHOICES = (
        ('local', 'local'),
        ('global', 'global'),
        ('swarm', 'swarm')
    )
    DRIVER_CHOICES = (
        ('host', 'host'),
        ('overlay', 'overlay'),
        ('null', 'null')
    )
    name = forms.CharField(
        max_length=20,
        label='Name',
        help_text="Name of the network",
        required=True
    )
    driver = forms.ChoiceField(
        choices=DRIVER_CHOICES,
        label='Driver',
        help_text='Name of the driver used to create the network',
        required=False
    )
    scope = forms.ChoiceField(
        choices=SCOPE_CHOICES,
        label='Scope',
        help_text='Specify the network’s scope (local, global or swarm)',
        required=False
    )


class ChangePasswordForm(forms.Form):
    password = forms.CharField(label="Password",max_length=20, widget=forms.PasswordInput)
    confirm = forms.CharField(label="Confirm Password",max_length=20, widget=forms.PasswordInput)


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput
                               )
    confirm = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
    )

    def confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords don't match")
        return password

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.confirm_password())
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'is_superuser',
                  'dashboard_permission',
                  'containers_permission',
                  'images_permission',
                  'networks_permission',
                  'volumes_permission',
                  'swarm_permission',
                  'events_permission'
                  ]
        labels = { 'username': 'Name', 'email': 'E-mail', }
        help_texts = {
            'email':'Please ensure the E-mail is available.',
        }
        error_messages= {
            'name':{
                'max_length': "The name is too long",
            },
        }

            


