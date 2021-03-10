from django import urls
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('api/',include('pro.api.urls'))
]