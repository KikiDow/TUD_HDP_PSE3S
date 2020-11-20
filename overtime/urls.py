from django.conf.urls import url, include
from .views import overtime_page

urlpatterns = [
    url(r'^overtime_page/$', overtime_page, name='overtime_page'),    
]