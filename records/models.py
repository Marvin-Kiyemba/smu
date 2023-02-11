from django.db import models

# Create your models here.

from assets.models import Asset
from users.models import User
from django.contrib import admin

from pygments.formatters.html import HtmlFormatter

class Record(models.Model):
    "Model representing an asset (but not a specific asset)"
    asset_name = models.ForeignKey('assets.Asset',on_delete=models.CASCADE, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.RESTRICT, help_text='Select staff', default='0')
    assigned_on = models.DateTimeField(auto_now_add=True)

    ASSET_STATUS = (
        ('a', 'Available'),
        ('n', 'Needs Maintenance'),
        ('d', 'Discontinued'),
        ('r', 'Returned'),
        ('x', 'Assigned'),
    )
    asset_status = models.CharField(max_length=1, choices=ASSET_STATUS, blank=True, default='a',help_text='Asset Availability')

    def __str__(self):
        """String for representing the model."""
        return f'({self.asset_name}) ({self.assigned_to})'

    def get_absolute_url(self):
        """Returns the URL to access a detail for this record"""
        return reversed('record-detail',args=[str(self.id)])

