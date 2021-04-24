from django.conf.urls import url, include
from .views import landing_page, clocking_page, generate_roster, view_personal_details, create_personal_details, edit_personal_details, my_notifications, clock, manual_clocking, view_manual_clock, view_submitted_manual_clockings, accept_manual_clock, reject_manual_clock, search_roster, previous_manual_clockings, search_manual_clocks, edit_manual_clock, delete_manual_clock, remote_clocking_page, view_remote_clockings, get_user_coords, view_individual_remote_clocking, view_lates, search_late_clockings

urlpatterns = [
    url(r'^$', landing_page, name='index'),
    url(r'^clocking_page/$', clocking_page, name='clocking_page'),
    #url(r'^generate_quarters/$', generate_quarters, name='generate_quarters'),
    url(r'^(?P<pk>\d+)/$', generate_roster, name='generate_roster'),
    url(r'^view_personal_details/$', view_personal_details, name='view_personal_details'),
    url(r'^create_personal_details/$', create_personal_details, name='create_personal_details'),
    url(r'^(?P<pk>\d+)/edit_personal_details/$', edit_personal_details, name='edit_personal_details'),
    url(r'^notifications$', my_notifications, name='my_notifications'),
    url(r'^clock/$', clock, name='clock'),
    url(r'^manual_clocking/$', manual_clocking, name='manual_clocking'),
    url(r'^(?P<pk>\d+)/view_manual_clock/$', view_manual_clock, name='view_manual_clock'),
    url(r'^view_submitted_manual_clockings/$', view_submitted_manual_clockings, name='view_submitted_manual_clockings'),
    url(r'^(?P<pk>\d+)/accept_manual_clock/$', accept_manual_clock, name='accept_manual_clock'),
    url(r'^(?P<pk>\d+)/reject_manual_clock/$', reject_manual_clock, name='reject_manual_clock'),
    url(r'^search_roster/$', search_roster, name='search_roster'),
    url(r'^previous_manual_clockings/$', previous_manual_clockings, name='previous_manual_clockings'),
    url(r'^search_manual_clocks/$', search_manual_clocks, name='search_manual_clocks'),
    url(r'^(?P<pk>\d+)/edit_manual_clock/$', edit_manual_clock, name='edit_manual_clock'),
    url(r'^(?P<pk>\d+)/delete_manual_clock/$', delete_manual_clock, name='delete_manual_clock'),
    url(r'^remote_clocking_page/$', remote_clocking_page, name='remote_clocking_page'),
    url(r'^view_remote_clockings/$', view_remote_clockings, name='view_remote_clockings'),
    url(r'^get_user_coords/$', get_user_coords, name='get_user_coords'),
    url(r'^(?P<pk>\d+)view_individual_remote_clocking/$', view_individual_remote_clocking, name='view_individual_remote_clocking'),
    url(r'^view_lates/$', view_lates, name='view_lates'),
    url(r'^search_late_clockings/$', search_late_clockings, name='search_late_clockings')
]