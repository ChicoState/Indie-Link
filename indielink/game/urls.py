# game/urls.py
from django.urls import path
from .views import create_game, game_list, game_detail, delete_games, create_dev_post, edit_dev_post, dev_post_detail

urlpatterns = [
    path('create_game/', create_game, name='create_game'),
    path('game_list/', game_list, name='game_list'),
    path('game_detail/<int:game_id>/', game_detail, name='game_detail'),
    path('delete_games/<int:game_id>/', delete_games, name='delete_games'),

    path('<int:game_id>/create_dev_post/', create_dev_post, name='create_dev_post'),
    path('<int:game_id>/edit_dev_post/<int:post_id>/', edit_dev_post, name='edit_dev_post'),
    path('<int:game_id>/dev_post/<int:post_id>/', dev_post_detail, name='dev_post_detail'),
]
