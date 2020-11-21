from django.conf.urls import url, include
from .views import exchanges_page

urlpatterns = [
    url(r'^exchanges_page/$', exchanges_page, name='exchanges_page'),  
]