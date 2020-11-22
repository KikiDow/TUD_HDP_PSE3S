from django.conf.urls import url, include
from .views import exchanges_page, submit_exchange_exchange_off, view_all_exchanges, previous_exchanges, submit_exchange_replacing_off_reply, submit_exchange_exchange_off_confirm, exchange_noticeboard, submit_post, like_post, cancel_exchange

urlpatterns = [
    url(r'^exchanges_page/$', exchanges_page, name='exchanges_page'),
    url(r'^submit_exchange_exchange_off/$', submit_exchange_exchange_off, name='submit_exchange_exchange_off'),
    url(r'^view_all_exchanges/$', view_all_exchanges, name='view_all_exchanges'),
    url(r'^previous_exchanges/$', previous_exchanges, name='previous_exchanges'),
    url(r'^(?P<pk>\d+)/submit_exchange_replacing_off_reply/$', submit_exchange_replacing_off_reply, name='submit_exchange_replacing_off_reply'),
    url(r'^(?P<pk>\d+)/submit_exchange_exchange_off_confirm/$', submit_exchange_exchange_off_confirm, name='submit_exchange_exchange_off_confirm'),
    url(r'^exchange_noticeboard/$', exchange_noticeboard, name='exchange_noticeboard'),
    url(r'^submit_post/$', submit_post, name='submit_post'),
    url(r'^(?P<pk>\d+)/like_post/$', like_post, name='like_post'),
    url(r'^(?P<pk>\d+)/cancel_exchange/$', cancel_exchange, name='cancel_exchange'),
]