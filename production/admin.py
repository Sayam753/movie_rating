from django.contrib import admin
from .models import ProfileOfProduction, ProfileOfActor, ProfileOfDirector, ProfileOfUser
# Register your models here.
admin.site.register(ProfileOfProduction)
admin.site.register(ProfileOfActor)
admin.site.register(ProfileOfDirector)
admin.site.register(ProfileOfUser)
