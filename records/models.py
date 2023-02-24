from django.db import models

# Create your models here.

from assets.models import Asset
from users.models import User
from django.contrib import admin

from pygments.formatters.html import HtmlFormatter

class Record(models.Model):
    "Model representing an asset (but not a specific asset)"
    asset_name = models.ForeignKey('assets.Asset',on_delete=models.CASCADE, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.RESTRICT, help_text='Select staff', default='0', related_name='assigned_user')
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
        

    def save(self, *args, **kwargs):
        #Get the asset associated with this record
        asset = self.asset_name

        #check if the asset is already assigned
        if asset.status == 'x':
            raise ValueError('Asset is already assigned')

        #if the asset is currrently available and the record is being saved with asset_status = "x",
        #update the asset status to "x" (assigned)
        if self.asset_status == 'x' and asset.status == 'a':
            asset.status = 'x'
            asset.save()

        #this calls the superclass savw() method to save the record
        super().save(*args, **kwargs)
