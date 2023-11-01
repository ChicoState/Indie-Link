from django import forms
from .models import Game, Genre

genres = []
for g in Genre.objects.all():
    genres.append((g.id, g.name))

class GameForm(forms.ModelForm):
    RELEASE_STATUS_CHOICES = (
        ('Released', 'Released'),
        ('In Development', 'In Development'),
        ('On Hold', 'On Hold'),
    )


    ## TODO: Find a more intuitive selection method than checkboxes
    genre = forms.MultipleChoiceField(choices = genres, widget=forms.CheckboxSelectMultiple())
    release_status = forms.ChoiceField(choices = RELEASE_STATUS_CHOICES, widget=forms.Select())
    cover_image = forms.ImageField(required=False)
    class Meta:
        model = Game
        fields = ['name', 'genre', 'description', 'release_status', 'cover_image']

class GenreSearchForm(forms.Form):
    genre = forms.ChoiceField(choices = genres)
