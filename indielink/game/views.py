# game/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import GameForm, GenreSearchForm, GameImageForm
from .models import Game, Genre, GameImage

@login_required
def create_game(request):
    if request.method == 'POST':
        game_form = GameForm(request.POST, request.FILES)
        image_form = GameImageForm(request.POST, request.FILES)
        if game_form.is_valid() and image_form.is_valid():
            game = game_form.save(commit=False)
            game.user = request.user
            game.save()
            game_form.save_m2m()
            for image in request.FILES.getlist('images'):
                GameImage.objects.create(game=game, game_image=image)
            return redirect('game_list')  # Redirect to 'game_list'
    else:
        game_form = GameForm()
        image_form = GameImageForm()

    page_data = {"game_form": game_form, 'image_form': image_form}
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


def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    game_images = GameImage.objects.filter(game=game)
    if request.user.is_authenticated:
        if request.user.favorite.filter(id = game_id).exists():
            fav = True
        else:
            fav = False
        return render(request, 'game/game_detail.html', {'game': game, 'fav':fav, 'game_images': game_images})
    return render(request, 'game/game_detail.html', {'game': game, 'game_images': game_images})

def delete_games(request):
    # Delete all games associated with the currently logged-in user
    #Game.objects.filter(user=request.user).delete()
    games = Game.objects.filter(user=request.user)
    for game in games:
        images = GameImage.objects.filter(game=game)
        for image in images:
            image.game_image.delete(save=False)
        images.delete()
        game.cover_image.delete()
    games.delete()
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
