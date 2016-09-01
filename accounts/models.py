from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField


class Account(models.Model):
    uuid = ShortUUIDField(unique=True)
    name = models.CharField(max_length=80)
    desc = models.TextField(blank=True)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    phone = models.CharField(max_length=10)
    owner = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'accounts'

    def __unicode__(self):
        return u"%s" % self.name

    @models.permalink
    def get_absolute_url(self):
        return 'account-details', [self.uuid]

    @models.permalink
    def get_update_url(self):
        return 'account-edit', [self.uuid]

    @models.permalink
    def get_delete_url(self):
        return 'account_delete', [self.uuid]
