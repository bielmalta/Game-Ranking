from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('buscar/', views.game_search, name='game_search'),
    path('ranking/', views.monthly_ranking, name='monthly_ranking'),
    path('genero/<int:genre_id>/', views.genre_games, name='genre_games'),
    path('jogo/<int:pk>/', views.game_detail, name='game_detail'),
]
