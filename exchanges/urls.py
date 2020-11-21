from django.conf.urls import url, include
from .views import exchanges_page, submit_exchange_exchange_off, view_all_exchanges, previous_exchanges

urlpatterns = [
    url(r'^exchanges_page/$', exchanges_page, name='exchanges_page'),
    url(r'^submit_exchange_exchange_off/$', submit_exchange_exchange_off, name='submit_exchange_exchange_off'),
    url(r'^view_all_exchanges/$', view_all_exchanges, name='view_all_exchanges'),
    url(r'^previous_exchanges/$', previous_exchanges, name='previous_exchanges'),
]