from django import forms

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
    ports = forms.CharField(max_length=100,
                            label='Ports',
                            help_text="Export Posts .For example, {'2222/tcp': 3333} will expose port 2222 inside the container as port 3333 on the host.",
                            required=False
                            )
    tty = forms.BooleanField(help_text='Allocate a pseudo-TTY.',
                             label='tty',
                             required=False
                             )
    work_dir = forms.CharField(max_length=100,
                               label="Working directory",
                               help_text="Path to the working directory.",
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
        label_suffix="Image Name e.g. ubuntu:14.04"
    )


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
    name = forms.CharField(
        max_length=20,
        label='Name',
        help_text="Network Name",
        required=True
    )
    driver = forms.CharField(
        max_length=30,
        label='Driver',
        help_text='Driver configuration',
        required=False
    )
