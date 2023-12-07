# game/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
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
def edit_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'GET':
        form = GameForm(instance=game)
        return render(request, 'game/edit.html', {"game_form": form})
    elif request.method == 'POST':
        form = GameForm(request.POST,request.FILES)
        form = GameForm(request.POST, files=request.FILES, instance=request.user)
        if (form.is_valid()):
            game.name = form.cleaned_data["name"]
            game.genre.set(form.cleaned_data["genre"]) #m2m field needs to be set seperately from other fields
            game.description = form.cleaned_data["description"]
            game.release_status = form.cleaned_data["release_status"]
            game.cover_image = form.cleaned_data["cover_image"]
            game.save(update_fields = ['name', 'description', 'release_status', 'cover_image'])
            return redirect('game_list')
        else:
            return render(request, 'game/edit.html', {"game_form": form})


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


def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.user.is_authenticated:
        if request.user.favorite.filter(id = game_id).exists():
            fav = True
        else:
            fav = False
        return render(request, 'game/game_detail.html', {'game': game, 'fav':fav})
    return render(request, 'game/game_detail.html', {'game': game})

def delete_games(request):
    # Delete all games associated with the currently logged-in user
    Game.objects.filter(user=request.user).delete()
    return redirect('game_list')

def add_fav(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    user = request.user
    user.favorite.add(game)
    ##This won't keep scroll posistion
    return HttpResponseRedirect("/game_detail/{game_id}/".format(game_id=game_id))

def remove_fav(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    user = request.user
    user.favorite.remove(game)
    return HttpResponseRedirect("/game_detail/{game_id}/".format(game_id=game_id))
