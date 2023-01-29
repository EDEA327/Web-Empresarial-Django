from django.urls import path
from . import views
#* Core Paths
urlpatterns = [
    path('',views.contact,name='contact'),
]