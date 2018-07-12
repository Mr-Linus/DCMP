from __future__ import absolute_import, unicode_literals
from celery import shared_task
from Dashboard.sys import sys


@shared_task
def deploy(image, command, auto_remove, tty, ports, working_dir, name):
    try:
        sys().client.containers.run(
            image=image,
            command=command,
            auto_remove=auto_remove,
            tty=tty,
            ports=ports,
            working_dir=working_dir,
            name=name)
        return True

    except:
        return False


@shared_task
def image_pull(image):
    try:
        sys().image.pull(image)
        return True

    except:
        return False