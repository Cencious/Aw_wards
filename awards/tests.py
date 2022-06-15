from django.test import TestCase
from .models import Profile,Project,Rating
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(username='kakan', password='zee12345')
        self.test_user.save()
        
    # def setUp(self):
        self.test_profile = Profile(User=self.test_user, bio='Never say never',name='cencious', profile_pic='cloudlink.cloud')

    def test_instance(self):
        self.assertTrue(isinstance(self.test_profile, Profile))


    def save_test(self):
        self.test_profile.save()
        self.assertEqual(len(Profile.objects.all()), 1)

    
    def tearDown(self):
        self.test_user.delete()
        


class RatingTestClass(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(username='kakan', password='zee12345')
        self.test_user.save()
        self.test_rating = Rating(user=self.test, project='News api', review='out_standing', rate_design=10, rate_usability=9, rate_content=8)

        
    def test_instance(self):
        self.assertTrue(isinstance(self.test_rating, Rating))

    def test_save(self):
        self.test_rating.save_comment()
        self.assertEqual(len(Rating.objects.all()), 1)
    

    def tearDown(self):
        self.test_user.delete()
        self.test_rating.delete()
        Rating.objects.all().delete()