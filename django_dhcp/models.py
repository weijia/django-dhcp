# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


class NetworkNode(models.Model):
    mac_address = models.CharField(max_length=12)
    ip = models.IPAddressField(help_text=_('ip address'))
    hostname = models.CharField(max_length=512)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s %s" % (self.mac_address, self.ip, self.hostname)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})