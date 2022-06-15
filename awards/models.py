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
        return self.name
    


class Project(models.Model):
    title = models.CharField(max_length=60)
    project_image =CloudinaryField('project_image', null=True)
    description = models.TextField()
    link = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    prof_ref = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_project(self):
        self.save()

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

    @classmethod
    def search_by_title(cls,search_term):
        '''
        method to search projects based on name
        '''
        
        title = cls.objects.filter(title__icontains=search_term).all()
        return title

    @classmethod
    def search_by_user(cls,user):
        projects = cls.objects.filter(user=user)
        return projects


class Rating(models.Model):
    RATE_CHOICES = [
    (10,'10-Outstanding'),
    (9,'9-Exceeds Expectations'),
    (8,'8-Excellent'),
    (7,'7-Good'),
    (6,'6-Barely Above Average'),
    (5,'5-Average'),
    (4,'4-Poor'),
    (3,'3-Awful'),
    (2,'2-Dreadful'),
    (1,'1-Troll'),
]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    review = models.TextField(null=True)
    rate_design = models.PositiveSmallIntegerField(choices = RATE_CHOICES)
    rate_usability = models.PositiveSmallIntegerField(choices = RATE_CHOICES)
    rate_content = models.PositiveSmallIntegerField(choices = RATE_CHOICES)


    def __str__(self):
        return self.user.username



    def save_rating(self):
        self.save()