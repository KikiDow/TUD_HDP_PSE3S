from django.conf.urls import url, include
from .views import overtime_page, allowances_page, submit_allowance_request, view_allowance_request, edit_allowance_request, delete_allowance_request, view_staff_allowance_requests, accept_allowance_request, reject_allowance_request, non_scheduled_ot_page, submit_nsot_request, view_non_scheduled_overtime_request, delete_nsot_request, edit_nsot_request, view_staff_nsot_requests, accept_nsot_request, reject_nsot_request, availability_page, submit_availability_sheet, view_availability_sheet, delete_availability_sheet, assign_ot_date, assign_ot_recall, assign_ot_require, search_allowances

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
    url(r'^submit_nsot_request/$', submit_nsot_request, name='submit_nsot_request'),
    url(r'^(?P<pk>\d+)view_non_scheduled_overtime_request/$', view_non_scheduled_overtime_request, name='view_non_scheduled_overtime_request'),
    url(r'^(?P<pk>\d+)/delete_nsot_request/$', delete_nsot_request, name='delete_nsot_request'),
    url(r'^(?P<pk>\d+)/edit_nsot_request/$', edit_nsot_request, name='edit_nsot_request'),
    url(r'^view_staff_nsot_requests/$', view_staff_nsot_requests, name='view_staff_nsot_requests'),
    url(r'^(?P<pk>\d+)/accept_nsot_request/$', accept_nsot_request, name='accept_nsot_request'),
    url(r'^(?P<pk>\d+)/reject_nsot_request/$', reject_nsot_request, name='reject_nsot_request'),
    url(r'^availability_page/$', availability_page, name='availability_page'),
    url(r'^submit_availability_sheet/$', submit_availability_sheet, name='submit_availability_sheet'),
    url(r'^(?P<pk>\d+)view_availability_sheet/$', view_availability_sheet, name='view_availability_sheet'),
    url(r'^(?P<pk>\d+)/delete_availability_sheet/$', delete_availability_sheet, name='delete_availability_sheet'),
    url(r'^assign_ot_date/$', assign_ot_date, name='assign_ot_date'),
    url(r'^(?P<chosen_date>\d{4}-\d{2}-\d{2})/assign_ot_recall/$', assign_ot_recall, name='assign_ot_recall'),
    url(r'^(?P<date_selected>\d{4}-\d{2}-\d{2})/assign_ot_require/$', assign_ot_require, name='assign_ot_require'),
    url(r'^search_allowances/$', search_allowances, name='search_allowances'),
]