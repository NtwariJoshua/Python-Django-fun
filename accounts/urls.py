from django.conf.urls import url
from . import views

account_urls = [

                url(r'^$', views.account_details, name='account-details'),
                url(r'edit/$', views.create_new_account, name='account-edit'),
                ]
