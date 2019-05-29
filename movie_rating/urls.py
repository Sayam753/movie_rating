from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from production import views as production_views
from django.conf import settings

urlpatterns = [

    path('', include('movie.urls')),
    path('admin/', admin.site.urls),
    path('register/', production_views.register,name="register"),
    path('profile_actor/', production_views.profile_for_actor,name="profile_actor"),
    path('profile_user/', production_views.profile_for_user,name="profile_user"),
    path('profile_director/', production_views.profile_for_director,name="profile_director"),
    path('profile_production/', production_views.profile_for_production,name="profile_production"),
    path('login/', auth_views.LoginView.as_view(template_name="production/login.html"),name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="production/logout.html"),name="logout"),
    #this include chops off whatever is written after blog/ and searches for the rest in the blog.urls patterns and finds the same the chopped off string in the patterns and calls that function.
]
