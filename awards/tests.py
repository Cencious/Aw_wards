from django.test import TestCase
from .models import Profile,Project,Rating
from django.contrib.auth.models import User

# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(username='kakan')

    def tearDown(self):
        self.test_user.delete()
        
    def setUp(self):
        self.test_profile = Profile(user='kakan', bio='Never say never', profile_pic='cloudlink.cloud')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))


class RatingTestClass(TestCase):
    def setUp(self):
        self.test_rating = Rating(user='kakan', project='News api', review='out_standing', rate_design=10, rate_usability=9, rate_content=8)

        
    def test_instance(self):
        self.assertTrue(isinstance(self.test_rating, Rating))

    def test_save(self):
        self.test_rating.save_comment()
        self.assertEqual(len(Rating.objects.all()), 1)
    

    def tearDown(self):
        self.test_user.delete()
        self.test_rating.delete()
        Rating.objects.all().delete()