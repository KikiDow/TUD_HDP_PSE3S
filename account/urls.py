from django.conf.urls import url, include
from .views import logout_view, login_view, home_page

urlpatterns = [
    url(r'^logout_view/$', logout_view, name='logout_view'),
    url(r'^login_view/$', login_view, name='login_view'),
    url(r'^home_page/$', home_page, name='home_page'),
]