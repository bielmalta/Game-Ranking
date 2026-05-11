from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from games.models import Game
from reviews.models import Rating


class RatingViewsTests(TestCase):
    def test_invalid_score_does_not_create_rating(self):
        user = User.objects.create_user(username='arthur', password='SenhaForte123')
        game = Game.objects.create(title='Invalid Score Game')
        self.client.force_login(user)

        response = self.client.post(reverse('rate_game', args=[game.pk]), {
            'score': 'abc',
        })

        self.assertRedirects(response, reverse('game_detail', args=[game.pk]))
        self.assertFalse(Rating.objects.filter(user=user, game=game).exists())
