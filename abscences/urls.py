from django.conf.urls import url, include
from .views import abscences_page, submit_csl, view_csl_application, delete_csl, edit_csl, submit_usl, view_usl_application, delete_usl, edit_usl, submit_fm, view_fm_application, delete_fm, edit_fm, view_staff_sick_leave_applications, view_my_sick_leave, accept_csl

urlpatterns = [
    url(r'^abscences_page/$', abscences_page, name='abscences_page'),
    url(r'^submit_csl/$', submit_csl, name='submit_csl'),
    url(r'^(?P<pk>\d+)/view_csl_application/$', view_csl_application, name='view_csl_application'),
    url(r'^(?P<pk>\d+)/delete_csl/$', delete_csl, name='delete_csl'),
    url(r'^(?P<pk>\d+)/edit_csl/$', edit_csl, name='edit_csl'),
    url(r'^submit_usl/$', submit_usl, name='submit_usl'),
    url(r'^(?P<pk>\d+)/view_usl_application/$', view_usl_application, name='view_usl_application'),
    url(r'^(?P<pk>\d+)/delete_usl/$', delete_usl, name='delete_usl'),
    url(r'^(?P<pk>\d+)/edit_usl/$', edit_usl, name='edit_usl'),
    url(r'^submit_fm/$', submit_fm, name='submit_fm'),
    url(r'^(?P<pk>\d+)/view_fm_application/$', view_fm_application, name='view_fm_application'),
    url(r'^(?P<pk>\d+)/delete_fm/$', delete_fm, name='delete_fm'),
    url(r'^(?P<pk>\d+)/edit_fm/$', edit_fm, name='edit_fm'),
    url(r'^view_staff_sick_leave_applications/$', view_staff_sick_leave_applications, name='view_staff_sick_leave_applications'),
    url(r'^view_my_sick_leave/$', view_my_sick_leave, name='view_my_sick_leave'),
    url(r'^(?P<pk>\d+)/accept_csl/$', accept_csl, name='accept_csl'),
]