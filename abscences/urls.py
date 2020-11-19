from django.conf.urls import url, include
from .views import abscences_page, submit_csl, view_csl_application, delete_csl, edit_csl, submit_usl, view_usl_application

urlpatterns = [
    url(r'^abscences_page/$', abscences_page, name='abscences_page'),
    url(r'^submit_csl/$', submit_csl, name='submit_csl'),
    url(r'^(?P<pk>\d+)/view_csl_application/$', view_csl_application, name='view_csl_application'),
    url(r'^(?P<pk>\d+)/delete_csl/$', delete_csl, name='delete_csl'),
    url(r'^(?P<pk>\d+)/edit_csl/$', edit_csl, name='edit_csl'),
    url(r'^submit_usl/$', submit_usl, name='submit_usl'),
    url(r'^(?P<pk>\d+)/view_usl_application/$', view_usl_application, name='view_usl_application')
]