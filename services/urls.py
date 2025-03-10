from django.urls import path

from services.views import *
urlpatterns =[
    path('',services_page,name='service')
]