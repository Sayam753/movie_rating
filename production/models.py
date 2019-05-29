from django.db import models
from django.contrib.auth.models import User
class ProfileOfProduction(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.user.username}'

class ProfileOfActor(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.user.username}'

    def max_rating(self):
        high=-1
        u = User.objects.filter(username=self.user.username).first()
        for r in u.profileofactor.newmovie_set.all():
            d = float(r.get_avg_rating)
            if (d > high):
                high = d
        if high == -1:
            return 'No rating given'
        else:
            return f'{high}'

    def min_rating(self):
        low=100
        u = User.objects.filter(username=self.user.username).first()
        for r in u.profileofactor.newmovie_set.all():
            d = float(r.get_avg_rating)
            if (d < low):
                low = d
        if low == 100:
            return 'No rating given'
        else:
            return f'{low}'

class ProfileOfDirector(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.user.username}'

    def max_rating(self):
        high=-1
        u = User.objects.filter(username=self.user.username).first()
        for r in u.profileofdirector.newmovie_set.all():
            d = float(r.get_avg_rating)
            if (d > high):
                high = d
        if high == -1:
            return 'No rating given'
        else:
            return f'{high}'

    def min_rating(self):
        low=100
        u = User.objects.filter(username=self.user.username).first()
        for r in u.profileofdirector.newmovie_set.all():
            d = float(r.get_avg_rating)
            if (d < low):
                low = d
        if low == 100:
            return 'No rating given'
        else:
            return f'{low}'

class ProfileOfUser(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.user.username}'

    def get_avg_rating(self):
        n=0
        sum=0.0
        u = User.objects.filter(username=self.user.username).first()
        for r in u.profileofuser.rate_set.all():
            sum += r.rating
            n+=1
        if n==0:
            return f'No rating given'
        else:
            return f'{sum/n}'

    def max_rating(self):
        high=-1
        u = User.objects.filter(username=self.user.username).first()
        for r in u.profileofuser.rate_set.all():
            if (r.rating > high):
                high = r.rating
        if high == -1:
            return 'No rating given'
        else:
            return f'{high}'

    def min_rating(self):
        low=100
        u = User.objects.filter(username=self.user.username).first()
        for r in u.profileofuser.rate_set.all():
            if (r.rating < low):
                low = r.rating
        if low == 100:
            return 'No rating given'
        else:
            return f'{low}'
