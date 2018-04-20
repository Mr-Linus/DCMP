from django.urls import path
from . import views
app_name = 'Dashboard'
urlpatterns = [
    path('', views.dashboard_login,name='login' ),
    path('logout/', views.dashboard_logout,name='logout'),
    path('index/', views.dashboard_index, name='index'),
]