from django.urls import path
from . import views
app_name = 'Dashboard'
urlpatterns = [
#  path('', views.dashboard_login,name='login' ),
    path('login/',views.dashboard_login_view.as_view()),
# path('logout/', views.dashboard_logout, name='logout'),
    path('logout/', views.dashboard_logout_view.as_view()),
# path('index/', views.dashboard_index, name='index'),
    path('index/', views.dashboard_index_view.as_view()),
    path('containers/', views.dashobard_containers_view),
    path('deploy/', views.dashboard_deploy_view),
    path('swarm/', views.dashobard_swarm_view),
    path('images/', views.dashobard_images_view),
    path('volumes/', views.dashboard_volume_view),
    path('networks/', views.dashboard_network_view),
    path('events/', views.dashboard_events_view.as_view()),
    path('settings/', views.dashboard_settings_view),
    path('add_update_user/', views.dashboard_add_update_view),
]
