from django.db import models

# Create your models here.

from users.models import User
from django.utils import timezone
from django.urls import reverse
from django.views import generic



class Asset(models.Model):
    asset_type = models.CharField(max_length=100)
    asset_code = models.CharField(max_length=100, help_text="Enter Number engraved on the Asset")
    asset_model = models.CharField(max_length=100)
    purchase_value = models.CharField(max_length=200, default='0')
    date_added = models.DateTimeField(default=timezone.now)

    ASSET_STATUS = (
        ('a', 'Available'),
        ('n', 'Needs Maintenance'),
        ('d', 'Discontinued'),
        ('r', 'Reserved'),
        ('x', 'Assigned'),

    )
    status = models.CharField(max_length=2, choices=ASSET_STATUS, blank=True, default = 'a', help_text='Asset Availability',)


    class Meta:
        ordering = ('asset_type','date_added')


    def get_absolute_url(self):
        """Returns the URL to access a particular instance of Asset."""
        return reverse('asset-detail-view')


    def __str__(self):
        return f'({self.asset_type}) ({self.asset_code})'
    
    
