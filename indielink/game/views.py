# game/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GameForm, GenreSearchForm
from .models import Game, Genre

@login_required
def create_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST,request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.user = request.user
            game.save()
            form.save_m2m()
            return redirect('game_list')  # Redirect to 'game_list'
    else:
        form = GameForm()

    page_data = {"game_form": form}
    return render(request, 'game/create_game.html', page_data)

@login_required
def game_list(request):
    games = Game.objects.all()
    return render(request, 'game/game_list.html', {'games': games})

def genre_search(request):
    if request.method == 'POST':
        if("search" in request.POST):
            search_form = GenreSearchForm(request.POST)
            if (search_form.is_valid()):
                search_genre = Genre.objects.get(id = search_form.cleaned_data['genre'])
                games = Game.objects.filter(genre__name = search_genre.name)
                page_data = {
                "genre": search_genre,
                "games": games
                }
                return render(request, 'game/search_results.html', page_data)
    else:
        search_form = GenreSearchForm()
        return render(request, 'game/genre_search.html', {'search_form': search_form})

@login_required
def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game/game_detail.html', {'game': game})

def delete_games(request):
    # Delete all games associated with the currently logged-in user
    Game.objects.filter(user=request.user).delete()
    return redirect('game_list')