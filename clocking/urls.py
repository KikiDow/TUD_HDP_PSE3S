from django.conf.urls import url, include
from .views import landing_page

urlpatterns = [
    url(r'^$', landing_page, name='index'),
]