from django.conf.urls import url, include
from .views import abscences_page, submit_csl, view_csl_application, delete_csl

urlpatterns = [
    url(r'^abscences_page/$', abscences_page, name='abscences_page'),
    url(r'^submit_csl/$', submit_csl, name='submit_csl'),
    url(r'^(?P<pk>\d+)/view_csl_application/$', view_csl_application, name='view_csl_application'),
    url(r'^(?P<pk>\d+)/delete_csl/$', delete_csl, name='delete_csl'),
]