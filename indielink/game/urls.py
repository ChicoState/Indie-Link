# game/urls.py
from django.urls import path
from .views import create_game, game_list, game_detail, delete_games, post_detail

urlpatterns = [
    path('create_game/', create_game, name='create_game'),
    path('post_detail/<int:game_id>/', post_detail, name='post_detail'), # Rename this URL pattern
    path('game_list/', game_list, name='game_list'),
    path('game_detail/<int:game_id>/', game_detail, name='game_detail'),
    path('delete_games/', delete_games, name='delete_games'),
]
