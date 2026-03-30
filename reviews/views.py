from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from games.models import Game
from .models import Rating, Comment

@login_required
def rate_game(request, pk):
    if request.method == 'POST':
        game  = get_object_or_404(Game, pk=pk)
        score = int(request.POST.get('score', 0))
        if 1 <= score <= 5:
            Rating.objects.update_or_create(
                user=request.user,
                game=game,
                defaults={'score': score},
            )
    return redirect('game_detail', pk=pk)

@login_required
def save_comment(request, pk):
    if request.method == 'POST':
        game = get_object_or_404(Game, pk=pk)
        body = request.POST.get('body', '').strip()
        if body:
            Comment.objects.update_or_create(
                user=request.user,
                game=game,
                defaults={'body': body},
            )
    return redirect('game_detail', pk=pk)