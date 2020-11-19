from django.conf.urls import url, include
from .views import abscences_page, submit_csl

urlpatterns = [
    url(r'^abscences_page/$', abscences_page, name='abscences_page'),
    url(r'^submit_csl/$', submit_csl, name='submit_csl'),
]