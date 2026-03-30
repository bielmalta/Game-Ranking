from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Game

def game_search(request):
    query = request.GET.get('q', '').strip()
    games = []
    searched = False

    if query:
        searched = True
        games = Game.objects.filter(
            Q(title__icontains=query)
        ).prefetch_related('genres')

    return render(request, 'games/search.html', {
        'games': games,
        'query': query,
        'searched': searched,
    })

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    comments = game.comments.select_related('user').order_by('-created_at')

    user_rating  = None
    user_comment = None

    if request.user.is_authenticated:
        user_rating  = game.ratings.filter(user=request.user).first()
        user_comment = game.comments.filter(user=request.user).first()

    return render(request, 'games/detail.html', {
        'game': game,
        'comments': comments,
        'user_rating': user_rating,
        'user_comment': user_comment,
        'star_range': range(1, 6),
    })