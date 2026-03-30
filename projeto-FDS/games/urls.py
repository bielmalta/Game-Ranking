from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_search, name='game_search'),
    path('game/<int:pk>/', views.game_detail, name='game_detail'),
]