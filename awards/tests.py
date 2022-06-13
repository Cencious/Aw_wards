from django.test import TestCase
from .models import Profile
from django.contrib.auth import User

# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='kakan')

    def tearDown(self):
        self.user.delete()
        