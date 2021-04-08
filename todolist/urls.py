
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = 'Todo Admin'
admin.site.site_title = 'Admin Portal'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls'))
]
