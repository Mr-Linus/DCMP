from django.urls import path
from . import views
app_name = 'Dashboard'
urlpatterns = [
  #  path('', views.dashboard_login,name='login' ),
    path('login/',views.dashboard_login.as_view()),
    # path('logout/', views.dashboard_logout, name='logout'),
    path('logout/', views.dashboard_logout.as_view()),
    path('index/', views.dashboard_index, name='index'),
]