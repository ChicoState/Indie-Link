# game/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import GameForm, GenreSearchForm, GameImageForm, DevPostForm
from .models import Game, Genre, GameImage, DevPost

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
def edit_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'GET':
        defaults = {'name': game.name, 'description': game.description, 'release_status': game.release_status, 'cover_image': game.cover_image}
        if game.genre:
            defaults['genre'] = [g.pk for g in game.genre.all()] #prefill genre field with game's genres
        form = GameForm(defaults, instance=game)
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

@login_required
def create_dev_post(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    
    if request.method == 'POST':
        form = DevPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.game = game
            blog_post.save()
            return redirect('game_detail', game_id=game_id)
    else:
        form = DevPostForm()

    return render(request, 'game/create_dev_post.html', {'form': form, 'game': game})

@login_required
def edit_dev_post(request, game_id, post_id):
    game = get_object_or_404(Game, pk=game_id)
    post = get_object_or_404(DevPost, pk=post_id, game=game)

    if request.method == 'POST':
        form = DevPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('game_detail', game_id=game_id)
    else:
        form = DevPostForm(instance=post)

    return render(request, 'game/edit_dev_post.html', {'form': form, 'game': game, 'post': post})

def dev_post_detail(request, game_id, post_id):
    game = get_object_or_404(Game, pk=game_id)
    post = get_object_or_404(DevPost, pk=post_id, game=game)
    
    return render(request, 'game/dev_post_detail.html', {'game': game, 'post': post})