from django.conf.urls import url, include
from .views import landing_page, clocking_page, generate_quarters, generate_roster, view_personal_details, create_personal_details, edit_personal_details

urlpatterns = [
    url(r'^$', landing_page, name='index'),
    url(r'^clocking_page/$', clocking_page, name='clocking_page'),
    url(r'^generate_quarters/$', generate_quarters, name='generate_quarters'),
    url(r'^(?P<pk>\d+)/$', generate_roster, name='generate_roster'),
    url(r'^view_personal_details/$', view_personal_details, name='view_personal_details'),
    url(r'^create_personal_details/$', create_personal_details, name='create_personal_details'),
    url(r'^(?P<pk>\d+)/edit_personal_details/$', edit_personal_details, name='edit_personal_details'),
]