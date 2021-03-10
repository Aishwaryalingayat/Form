from django.urls import path
from . import views

urlpatterns=[
    path('get-tickiting-tools/',views.GetTickitingToolProjectList.as_view(), name='get_tickiting_tools'),
    path('add-tickiting-tools/',views.AddTickitingToolProjectList.as_view(), name='add_tickiting_tools'),
]