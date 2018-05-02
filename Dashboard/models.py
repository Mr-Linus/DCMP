from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.


class DashboardUserManager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('containers_permission', True)
        extra_fields.setdefault('images_permission', True)
        extra_fields.setdefault('networks_permission', True)
        extra_fields.setdefault('volumes_permission', True)
        extra_fields.setdefault('swarm_permission', True)
        extra_fields.setdefault('events_permission', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    dashboard_permission = models.BooleanField(default=True,
                                               verbose_name="Dashboard Permission"
                                               )
    containers_permission = models.BooleanField(default=False,
                                                verbose_name="Containers Permission"
                                                )
    images_permission = models.BooleanField(default=False,
                                            verbose_name="Images Permission"
                                            )
    networks_permission = models.BooleanField(default=False,
                                              verbose_name="Networks Permission"
                                              )
    volumes_permission = models.BooleanField(default=False,
                                             verbose_name="Volumes Permission"
                                             )
    swarm_permission = models.BooleanField(default=False,
                                           verbose_name="Swarm Permission"
                                           )
    events_permission = models.BooleanField(default=False,
                                            verbose_name="Events Permission"
                                            )
    objects = DashboardUserManager()
