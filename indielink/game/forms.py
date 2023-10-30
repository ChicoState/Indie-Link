from django import forms
<<<<<<< HEAD
from .models import Game, Genre

# Comment out genres, migrate, uncomment

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
=======
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'genre', 'description']
>>>>>>> 0d8ef7b (Adds user game entries, display and delete)
