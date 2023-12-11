from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from game.models import Game, Genre  # Import the Game model from the 'game' app

def landingpage(request):
    genres = Genre.objects.all()  # Fetch all genres from the database
    games_by_genre = {genre: Game.objects.filter(genre=genre) for genre in genres}
    return render(request, 'landing/discov.html', {'games_by_genre': games_by_genre})
@login_required
def favorites(request):
    games = request.user.favorite.all()
    return render(request, 'landing/favorites.html', {'games': games})
