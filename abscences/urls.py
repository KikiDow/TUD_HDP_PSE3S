from django.conf.urls import url, include
from .views import abscences_page

urlpatterns = [
    url(r'^abscences_page/$', abscences_page, name='abscences_page'),    
]