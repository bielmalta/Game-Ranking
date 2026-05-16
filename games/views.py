from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Game, Genre, PlayedGame


def monthly_ranking_queryset():
    now = timezone.localtime()
    return (
        Game.objects.annotate(
            monthly_ratings=Count(
                'ratings',
                filter=Q(
                    ratings__updated_at__year=now.year,
                    ratings__updated_at__month=now.month,
                ),
                distinct=True,
            )
        )
        .filter(monthly_ratings__gt=0)
        .prefetch_related('genres')
        .order_by('-monthly_ratings', 'title')
    )


def overall_ranking_queryset():
    return (
        Game.objects.annotate(total_ratings=Count('ratings', distinct=True))
        .filter(total_ratings__gt=0)
        .prefetch_related('genres')
        .order_by('-total_ratings', 'title')
    )


def home(request):
    ranking_queryset = monthly_ranking_queryset()
    featured_games = Game.objects.prefetch_related('genres').order_by('?')[:10]
    genres = Genre.objects.filter(game__isnull=False).distinct().order_by('name')
    ranking_date = timezone.localtime()

    return render(request, 'games/home.html', {
        'top_ranked_games': ranking_queryset[:3],
        'show_full_ranking_link': ranking_queryset.count() > 3,
        'featured_games': featured_games,
        'genres': genres,
        'ranking_period': ranking_date.strftime('%m/%Y'),
    })


def game_search(request):
    query = request.GET.get('q', '').strip()
    games = Game.objects.none()

    if query:
        games = (
            Game.objects.filter(Q(title__icontains=query))
            .prefetch_related('genres')
            .order_by('title')
        )

    return render(request, 'games/search.html', {
        'games': games,
        'query': query,
        'searched': bool(query),
    })


def monthly_ranking(request):
    ranking_date = timezone.localtime()
    ranking_games = list(monthly_ranking_queryset()[:20])
    is_monthly_ranking = True

    if not ranking_games:
        ranking_games = list(overall_ranking_queryset()[:20])
        is_monthly_ranking = False

    return render(request, 'games/ranking.html', {
        'ranking_games': ranking_games,
        'ranking_period': ranking_date.strftime('%m/%Y'),
        'is_monthly_ranking': is_monthly_ranking,
    })


def genre_games(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    games = (
        Game.objects.filter(genres=genre)
        .prefetch_related('genres')
        .distinct()
        .order_by('title')
    )

    return render(request, 'games/genre_games.html', {
        'genre': genre,
        'games': games,
    })


def game_detail(request, pk):
    game = get_object_or_404(Game.objects.prefetch_related('genres'), pk=pk)
    comments = game.comments.select_related('user').order_by('-created_at')

    user_rating = None
    user_comment = None
    is_played = False

    if request.user.is_authenticated:
        user_rating = game.ratings.filter(user=request.user).first()
        user_comment = game.comments.filter(user=request.user).first()
        is_played = PlayedGame.objects.filter(user=request.user, game=game).exists()

    return render(request, 'games/detail.html', {
        'game': game,
        'comments': comments,
        'user_rating': user_rating,
        'user_comment': user_comment,
        'is_played': is_played,
        'star_range': range(1, 6),
    })


@login_required
def toggle_played(request, pk):
    if request.method == 'POST':
        game = get_object_or_404(Game, pk=pk)
        existing = PlayedGame.objects.filter(user=request.user, game=game).first()
        if existing:
            existing.delete()
        else:
            PlayedGame.objects.create(user=request.user, game=game)
    return redirect('game_detail', pk=pk)
