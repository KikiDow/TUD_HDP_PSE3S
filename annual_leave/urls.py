from django.conf.urls import url, include
from .views import annual_leave_page

urlpatterns = [
    url(r'^annual_leave_page/$', annual_leave_page, name='annual_leave_page'),    
]