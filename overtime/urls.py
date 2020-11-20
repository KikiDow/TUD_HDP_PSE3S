from django.conf.urls import url, include
from .views import overtime_page, allowances_page, submit_allowance_request, view_allowance_request, edit_allowance_request, delete_allowance_request, view_staff_allowance_requests, accept_allowance_request, reject_allowance_request, non_scheduled_ot_page

urlpatterns = [
    url(r'^overtime_page/$', overtime_page, name='overtime_page'),
    url(r'^allowances_page/$', allowances_page, name='allowances_page'),
    url(r'^submit_allowance_request/$', submit_allowance_request, name='submit_allowance_request'),
    url(r'^(?P<pk>\d+)view_allowance_request/$', view_allowance_request, name='view_allowance_request'),
    url(r'^(?P<pk>\d+)/edit_allowance_request/$', edit_allowance_request, name='edit_allowance_request'),
    url(r'^(?P<pk>\d+)/delete_allowance_request/$', delete_allowance_request, name='delete_allowance_request'),
    url(r'^view_staff_allowance_requests/$', view_staff_allowance_requests, name='view_staff_allowance_requests'),
    url(r'^(?P<pk>\d+)/accept_allowance_request/$', accept_allowance_request, name='accept_allowance_request'),
    url(r'^(?P<pk>\d+)/reject_allowance_request/$', reject_allowance_request, name='reject_allowance_request'),
    url(r'^non_scheduled_ot_page/$', non_scheduled_ot_page, name='non_scheduled_ot_page'),
]