"""PSE3S URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from clocking.views import landing_page
from account import urls as account_urls
from clocking import urls as clocking_urls
from annual_leave import urls as annual_leave_urls
from abscences import urls as abscences_urls
from overtime import urls as overtime_urls
import notifications.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', landing_page, name='index'),
    url(r'^account/', include(account_urls)),
    url(r'^clocking/', include(clocking_urls)),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    url(r'^annual_leave/', include(annual_leave_urls)),
    url(r'^abscences/', include(abscences_urls)),
     url(r'^overtime/', include(overtime_urls)),
]
