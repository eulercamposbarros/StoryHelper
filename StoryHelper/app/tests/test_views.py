import django
from django.test import TestCase
from app.models import *

class ViewTest(TestCase):
    if django.VERSION[:2] >= (1, 7):
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        response = self.client.get('/')
        self.assertContains(response, 'Story Helper', status_code=200)

