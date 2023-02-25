
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='conatct'),
    path('admin/', admin.site.urls),
]
