from django import forms

class DeployForm(forms.Form):
    name = forms.CharField(max_length=100, label='Contianer Name', help_text="Please input the Container name.This is a custom option", required=False)
    image = forms.CharField(max_length=100, label='Image', help_text="This is a required option", required=True)
    auto_remove = forms.BooleanField(help_text="Automatically close the container when a problem occurs", label="Auto remove", required=False)
    ports = forms.CharField(max_length=100, label='Ports', help_text="Export Posts .For example, {'2222/tcp': 3333} will expose port 2222 inside the container as port 3333 on the host.", required=False)
    tty = forms.BooleanField(help_text='Allocate a pseudo-TTY.', label='tty', required=False)
    work_dir = forms.CharField(max_length=100, label="Working directory", help_text="Path to the working directory.", required=False)
    cmd = forms.CharField(max_length=100, label='Command',help_text="The command to run in the container.", required=False)



