from django import template
from production.models import ProfileOfUser
from movie.models import NewMovie

register = template.Library()

@register.filter(name='has_already_rated')
def has_already_rated(user, object):
    for r in user.profileofuser.rate_set.all():
        if (r.m.id==object):
            return True
    return False
