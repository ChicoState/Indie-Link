# game/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GameForm
from .models import Game

@login_required
def create_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.user = request.user
            game.save()
            return redirect('game_list')  # Redirect to 'game_list'
    else:
        form = GameForm()

    page_data = {"game_form": form}
    return render(request, 'game/create_game.html', page_data)

@login_required
def game_list(request):
    games = Game.objects.all()
    return render(request, 'game/game_list.html', {'games': games})

@login_required
def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game/game_detail.html', {'game': game})

def delete_games(request):
    # Delete all games associated with the currently logged-in user
    Game.objects.filter(user=request.user).delete()
    return redirect('game_list')