from django.conf.urls import url, include
from .views import exchanges_page, submit_exchange_exchange_off

urlpatterns = [
    url(r'^exchanges_page/$', exchanges_page, name='exchanges_page'),
    url(r'^submit_exchange_exchange_off/$', submit_exchange_exchange_off, name='submit_exchange_exchange_off'),
]