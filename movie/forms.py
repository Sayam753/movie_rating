from django import forms
from movie.models import NewMovie, Rate
from production.models import ProfileOfActor, ProfileOfDirector

class NewMovieForm(forms.ModelForm):
    directors = forms.ModelMultipleChoiceField(widget=forms.widgets.SelectMultiple(), queryset=ProfileOfDirector.objects.all())
    actors = forms.ModelMultipleChoiceField(widget=forms.widgets.SelectMultiple(), queryset=ProfileOfActor.objects.all())
    class Meta:
        model = NewMovie
        fields = ('title','description','directors','actors')

class ReRateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('rating',)
