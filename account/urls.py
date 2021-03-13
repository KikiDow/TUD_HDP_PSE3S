from django.conf.urls import url, include
from .views import logout_view, login_view, home_page, registration, view_new_account, delete_account, edit_new_account, generate_quarters

urlpatterns = [
    url(r'^logout_view/$', logout_view, name='logout_view'),
    url(r'^login_view/$', login_view, name='login_view'),
    url(r'^home_page/$', home_page, name='home_page'),
    url(r'^registration/$', registration, name='registration'),
    url(r'^(?P<pk>\d+)/$', view_new_account, name='view_new_account'),
    url(r'^(?P<pk>\d+)/delete_account/$', delete_account, name='delete_account'),
    url(r'^(?P<pk>\d+)/edit_new_account/$', edit_new_account, name='edit_new_account'),
    url(r'^generate_quarters/$', generate_quarters, name='generate_quarters'),
]