from django.conf.urls import url, include
from .views import landing_page, clocking_page, generate_quarters, generate_roster, view_personal_details, create_personal_details, edit_personal_details, my_notifications, clock, manual_clocking, view_manual_clock

urlpatterns = [
    url(r'^$', landing_page, name='index'),
    url(r'^clocking_page/$', clocking_page, name='clocking_page'),
    url(r'^generate_quarters/$', generate_quarters, name='generate_quarters'),
    url(r'^(?P<pk>\d+)/$', generate_roster, name='generate_roster'),
    url(r'^view_personal_details/$', view_personal_details, name='view_personal_details'),
    url(r'^create_personal_details/$', create_personal_details, name='create_personal_details'),
    url(r'^(?P<pk>\d+)/edit_personal_details/$', edit_personal_details, name='edit_personal_details'),
    url(r'^notifications$', my_notifications, name='my_notifications'),
    url(r'^clock/$', clock, name='clock'),
    url(r'^manual_clocking/$', manual_clocking, name='manual_clocking'),
    url(r'^(?P<pk>\d+)/$', view_manual_clock, name='view_manual_clock'),
]