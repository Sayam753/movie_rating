from django.urls import path
from .views import MovieListView, PostDetailView, PostCreateView, UserPostListView, RateCreateView, RateUpdateView
from . import views
urlpatterns = [
    path('movie/<int:pk>/re_rate/',RateUpdateView.as_view(),name='re_rate'),
    path('', MovieListView.as_view(),name='movie_home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('movie/<int:pk>/', PostDetailView.as_view(),name='post_detail'),
    path('movie/<int:pk>/rate/', RateCreateView.as_view(),name='movie_update'),
    path('about/', views.about,name='movie_about'),
    path('movie/new/', PostCreateView,name='post_create'),
]
