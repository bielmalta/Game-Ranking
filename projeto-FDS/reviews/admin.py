from django.contrib import admin
from .models import Rating, Comment

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'score')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'created_at')
    search_fields = ('user__username', 'game__title')