from django.conf.urls import url, include
from .views import landing_page, clocking_page, generate_quarters

urlpatterns = [
    url(r'^$', landing_page, name='index'),
    url(r'^clocking_page/$', clocking_page, name='clocking_page'),
    url(r'^generate_quarters/$', generate_quarters, name='generate_quarters'),
]