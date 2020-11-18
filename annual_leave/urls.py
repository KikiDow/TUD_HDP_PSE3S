from django.conf.urls import url, include
from .views import annual_leave_page, block_leave_request

urlpatterns = [
    url(r'^annual_leave_page/$', annual_leave_page, name='annual_leave_page'),
    url(r'^block_leave_request/$', block_leave_request, name='block_leave_request'),
]