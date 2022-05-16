
from django.contrib import admin
from django.urls import include, path

from company.views import *

urlpatterns = [

    path('', include('company.urls')),
]

