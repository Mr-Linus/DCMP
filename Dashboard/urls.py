from django.urls import path
from . import views
app_name = 'Dashboard'
urlpatterns = [
    path('' , views.dashboard_login ),
    path('logout/',views.dashboard_logout)
]