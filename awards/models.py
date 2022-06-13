from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE,related_name='Profile')
    bio = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=120)
    profile_pic = CloudinaryField('image')
    # phone_number = PhoneField(max_length=15, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} Profile'


class Project(models.Model):
    title = models.CharField(max_length=60)
    project_image =CloudinaryField('project_image', null=True)
    description = models.TextField()
    link = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    prof_ref = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects', null=True)

    class Meta:
        ordering =['pub_date']
    
    def __str__(self):
        return self.title
    
    def no_of_ratings(self):
        ratings = Rating.objects.all(project=self)
        return len(ratings)
    

    def average_ratings(self):
        sum = 0
        ratings = Rating.objects.filter(project=self)
        for rating in ratings:
            sum += ((rating.rate_design + rating.rate_usability + rating.rate_content)/3)
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0