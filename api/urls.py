from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('provider/', provider_list_create_view),
    path('provider/<provider_id>/', provider_retrive_update_view),
    path('service_area/', service_area_list_create_view),
    path('service_area/<service_area>/', service_area_list_create_view),
]
