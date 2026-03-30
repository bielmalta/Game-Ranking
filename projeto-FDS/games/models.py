from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'


class Game(models.Model):
    title       = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(blank=True, verbose_name='Descrição')
    release_year = models.PositiveIntegerField(null=True, blank=True, verbose_name='Ano de lançamento')
    cover       = models.ImageField(upload_to='covers/', blank=True, verbose_name='Capa')
    trailer_url = models.URLField(blank=True, verbose_name='URL do trailer (YouTube embed)')
    official_url = models.URLField(blank=True, verbose_name='Site oficial')
    genres      = models.ManyToManyField(Genre, blank=True, verbose_name='Gêneros')

    def __str__(self):
        return self.title

    def average_rating(self):
        ratings = self.ratings.all()
        if not ratings.exists():
            return None
        return round(sum(r.score for r in ratings) / ratings.count(), 1)

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
        ordering = ['title']