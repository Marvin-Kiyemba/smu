from django.test import TestCase

# Create your tests here.
import datetime
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from assets.models import Asset

class RecordModelTests(TestCase):

    def asset_was_added_recently_with_future_assignment(self):
        """
        was_added_recently() returns False for assets that are not assigned
        """
