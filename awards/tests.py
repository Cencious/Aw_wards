from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='kakan')

    def tearDown(self):
        self.user.delete()
        
    def setUp(self):
        self.profile = Profile(user='kakan', bio='Never say never', profile_pic='cloudlink.cloud')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))