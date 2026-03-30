from django.contrib import admin
from .models import Game, Genre

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