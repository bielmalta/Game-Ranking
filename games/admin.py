from django.contrib import admin
from .models import Game, Genre, PlayedGame

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display  = ('title', 'release_year', 'average_rating')
    search_fields = ('title',)
    list_filter   = ('genres',)
    filter_horizontal = ('genres',)
    fields = (
        'title',
        'description',
        'release_year',
        'cover',
        'cover_url',
        'trailer_url',
        'official_url',
        'genres',
    )


@admin.register(PlayedGame)
class PlayedGameAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'played_at')
    list_filter = ('played_at',)
    search_fields = ('user__username', 'game__title')
