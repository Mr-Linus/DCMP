from django.urls import path
from . import views
app_name = 'Promotion'
urlpatterns = [
    path('', views.index, name='index'),
]