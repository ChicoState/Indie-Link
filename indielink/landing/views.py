from django.shortcuts import render
from game.models import Game  # Import the Game model from the 'game' app

def landingpage(request):
    games = Game.objects.all()  # Fetch all games from the database
    return render(request, 'landing/discov.html', {'games': games})
