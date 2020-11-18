from django.conf.urls import url, include
from .views import annual_leave_page, block_leave_request, view_annual_leave_request, short_term_leave_request, view_st_leave_request

urlpatterns = [
    url(r'^annual_leave_page/$', annual_leave_page, name='annual_leave_page'),
    url(r'^block_leave_request/$', block_leave_request, name='block_leave_request'),
    url(r'^(?P<pk>\d+)/view_annual_leave_request/$', view_annual_leave_request, name='view_annual_leave_request'),
    url(r'^short_term_leave_request/$', short_term_leave_request, name='short_term_leave_request'),
    url(r'^(?P<pk>\d+)/view_st_leave_request/$', view_st_leave_request, name='view_st_leave_request'),
]