"""simple_crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from marketting import views
from subscribers.views import subscribe_new
from accounts.views import AccountList
from accounts.urls import account_urls
from accounts.views import create_new_account


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name="home"),
    url(r'^sign-up/$', subscribe_new, name="signup"),
    url(r'^login$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^account/list', AccountList.as_view(), name='account-list'),
    url(r'^account/new/$', create_new_account, name='new-account'),
    url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),


]
