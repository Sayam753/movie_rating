from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from production.models import ProfileOfActor, ProfileOfDirector, ProfileOfUser
from django.urls import reverse
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class NewMovie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    directors = models.ManyToManyField(ProfileOfDirector)
    actors = models.ManyToManyField(ProfileOfActor)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    @property
    def get_avg_rating(self):
        sum=0.0
        n=0
        for i in self.rate_set.all():
            n +=1
            sum += i.rating
        if (n==0):
            return '0'
        else:
            return f'{sum/n}'

class Rate(models.Model):
    m = models.ForeignKey(NewMovie,on_delete = models.CASCADE)
    u = models.ForeignKey(ProfileOfUser,on_delete = models.CASCADE)
    rating = models.FloatField(null=True, blank=True, default=0,validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    rated_on = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return f'{self.rating}'
    def get_absolute_url(self):
        return reverse('movie_home')
