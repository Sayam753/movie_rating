from django import template
from production.models import ProfileOfUser
from movie.models import NewMovie

register = template.Library()

@register.filter(name='capture_rating')
def capture_rating(user, object):
    for r in user.profileofuser.rate_set.all():
        if (r.m.id==object):
            return r.rating
