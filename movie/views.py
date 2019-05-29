from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from production.models import ProfileOfUser
from movie.models import NewMovie, Rate
from movie import forms
from movie.templates import movie
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import FormView

def PostCreateView(request):
    if request.method == "POST":
        form = forms.NewMovieForm(request.POST)
        context = {'form': form}
        form.instance.author = request.user
        m = form.save(commit=False)
        m.save()
        m.directors.set(form.cleaned_data.get("directors"))
        m.actors.set(form.cleaned_data.get("actors"))
        form.save_m2m()
        return redirect('movie_home')

    form = forms.NewMovieForm()
    context = {'form': form}
    return render(request,'movie/new_movie_form.html',context)

class MovieListView(ListView):
    model = NewMovie
    template_name = 'movie/home.html'
    context_object_name = 'movies';
    ordering = ['-release_date']

class UserPostListView(ListView):
    model = NewMovie
    template_name = 'movie/production_movie.html'
    context_object_name = 'movies';
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return NewMovie.objects.filter(author=user).order_by('-release_date')

class RateUpdateView(LoginRequiredMixin,FormView):
    template_name = 'movie/rate_form.html'
    form_class = forms.ReRateForm
    success_url='/'
    def form_valid(self, form):
        u = self.request.user
        for mo in u.profileofuser.rate_set.all():
            if(mo.m.id==self.kwargs['pk']):
                mo.rating = form.cleaned_data.get('rating')
                mo.save()
                break
        return super().form_valid(form)


class RateCreateView(LoginRequiredMixin, CreateView):
    model = Rate
    fields=['rating']
    template_name = 'movie/rate_form.html'
    def form_valid(self,form):
        p = ProfileOfUser.objects.filter(user=self.request.user).first()
        mov_id = NewMovie.objects.filter(id=self.kwargs['pk']).first()
        form.instance.u = p
        form.instance.m = mov_id
        form.save()
        return super().form_valid(form)
    def test_func(self):
        return True


class PostDetailView(DetailView):
    template_name = 'movie/new_movie_detail.html'
    model = NewMovie

def about(request):
    return render(request,'movie/about.html')
