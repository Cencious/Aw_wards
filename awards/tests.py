from django.test import TestCase
from .models import Profile
from django.contrib.auth import User

# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='kakan')

    def tearDown(self):
        self.user.delete()
        
    def test_new_profile(self):
        self.assertIsInstance(self.user.profile, Profile)
        self.user.save()
        self.assertIsInstance(self.user.profile, Profile)