from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from game.models import Game  # Import the Game model from the 'game' app

def landingpage(request):
    games = Game.objects.all()  # Fetch all games from the database
    return render(request, 'landing/discov.html', {'games': games})

@login_required
def favorites(request):
    games = request.user.favorite.all()
    return render(request, 'landing/favorites.html', {'games': games})
