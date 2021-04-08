from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('del_task', views.del_task,name='del_task'),
    
]
