from django import forms
from .models import Game, Genre

genres = []
for g in Genre.objects.all():
    genres.append((g.id, g.name))

class GameForm(forms.ModelForm):
    ## TODO: Find a more intuitive selection method than checkboxes
    genre = forms.MultipleChoiceField(choices = genres, widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Game
        fields = ['name', 'genre', 'description']

class GenreSearchForm(forms.Form):
    genre = forms.ChoiceField(choices = genres)
