from urllib.parse import parse_qs, urlparse

from django.contrib.auth.models import User
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'


class Game(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(blank=True, verbose_name='Descrição')
    release_year = models.PositiveIntegerField(null=True, blank=True, verbose_name='Ano de lançamento')
    cover = models.ImageField(upload_to='covers/', blank=True, verbose_name='Capa')
    cover_url = models.URLField(blank=True, verbose_name='Link da capa')
    trailer_url = models.URLField(blank=True, verbose_name='URL do trailer (YouTube embed)')
    official_url = models.URLField(blank=True, verbose_name='Site oficial')
    genres = models.ManyToManyField(Genre, blank=True, verbose_name='Gêneros')

    def __str__(self):
        return self.title

    def average_rating(self):
        ratings = self.ratings.all()
        if not ratings.exists():
            return None
        return round(sum(r.score for r in ratings) / ratings.count(), 1)

    @property
    def cover_source(self):
        if self.cover:
            return self.cover.url
        if self.cover_url:
            return self.cover_url
        return ''

    @property
    def trailer_embed_url(self):
        url = self.trailer_url.strip()
        if not url:
            return ''

        parsed = urlparse(url)
        host = parsed.netloc.lower()
        if host.startswith('www.'):
            host = host[4:]

        video_id = ''
        if host in ('youtube.com', 'm.youtube.com'):
            if parsed.path == '/watch':
                video_id = parse_qs(parsed.query).get('v', [''])[0]
            elif parsed.path.startswith('/embed/'):
                video_id = parsed.path.split('/embed/', 1)[1].split('/')[0]
            elif parsed.path.startswith('/shorts/'):
                video_id = parsed.path.split('/shorts/', 1)[1].split('/')[0]
        elif host == 'youtu.be':
            video_id = parsed.path.strip('/').split('/')[0]

        if video_id:
            return f'https://www.youtube.com/embed/{video_id}'
        return url

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
        ordering = ['title']


class PlayedGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='played_games')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='played_by')
    played_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')
        ordering = ['-played_at']
        verbose_name = 'Jogo jogado'
        verbose_name_plural = 'Jogos jogados'

    def __str__(self):
        return f'{self.user} jogou {self.game}'
