from django.conf.urls import url, include
from .views import annual_leave_page, block_leave_request, view_annual_leave_request, short_term_leave_request, view_st_leave_request, delete_block_leave_request, edit_block_leave_request, delete_short_term_leave_request, edit_short_term_leave_request, view_my_leave_requests, view_staff_leave_submissions, accept_block_leave, reject_annual_leave, accept_short_term_leave, reject_short_term_leave, search_annual_leave

urlpatterns = [
    url(r'^annual_leave_page/$', annual_leave_page, name='annual_leave_page'),
    url(r'^block_leave_request/$', block_leave_request, name='block_leave_request'),
    url(r'^(?P<pk>\d+)/view_annual_leave_request/$', view_annual_leave_request, name='view_annual_leave_request'),
    url(r'^(?P<pk>\d+)/edit_block_leave_request/$', edit_block_leave_request, name='edit_block_leave_request'),
    url(r'^(?P<pk>\d+)/delete_block_leave_request/$', delete_block_leave_request, name='delete_block_leave_request'),
    url(r'^short_term_leave_request/$', short_term_leave_request, name='short_term_leave_request'),
    url(r'^(?P<pk>\d+)/view_st_leave_request/$', view_st_leave_request, name='view_st_leave_request'),
    url(r'^(?P<pk>\d+)/delete_short_term_leave_request/$', delete_short_term_leave_request, name='delete_short_term_leave_request'),
    url(r'^(?P<pk>\d+)/edit_short_term_leave_request/$', edit_short_term_leave_request, name='edit_short_term_leave_request'),
    url(r'^view_my_leave_requests/$', view_my_leave_requests, name='view_my_leave_requests'),
    url(r'^view_staff_leave_submissions/$', view_staff_leave_submissions, name='view_staff_leave_submissions'),
    url(r'^(?P<pk>\d+)/accept_block_leave/$', accept_block_leave, name='accept_block_leave'),
    url(r'^(?P<pk>\d+)/reject_annual_leave/$', reject_annual_leave, name='reject_annual_leave'),
    url(r'^(?P<pk>\d+)/accept_short_term_leave/$', accept_short_term_leave, name='accept_short_term_leave'),
    url(r'^(?P<pk>\d+)/reject_short_term_leave/$', reject_short_term_leave, name='reject_short_term_leave'),
    url(r'^search_annual_leave/$', search_annual_leave, name='search_annual_leave')
]