from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from games.models import Game, Genre
from reviews.models import Rating


class GameModelTests(TestCase):
    def test_cover_source_uses_cover_url_when_local_cover_file_is_missing(self):
        game = Game(
            title='Missing Cover Game',
            cover='covers/missing-cover.jpg',
            cover_url='https://example.com/fallback.jpg',
        )

        self.assertEqual(game.cover_source, 'https://example.com/fallback.jpg')

    def test_cover_source_is_empty_when_local_cover_file_is_missing_without_fallback(self):
        game = Game(
            title='Missing Cover Game',
            cover='covers/missing-cover.jpg',
        )

        self.assertEqual(game.cover_source, '')

    def test_trailer_embed_url_converts_youtube_watch_url(self):
        game = Game(
            title='Trailer Game',
            trailer_url='https://www.youtube.com/watch?v=pBM2xyco_Kg&vl=en',
        )

        self.assertEqual(
            game.trailer_embed_url,
            'https://www.youtube.com/embed/pBM2xyco_Kg',
        )

    def test_trailer_embed_url_converts_short_youtube_url(self):
        game = Game(
            title='Short Trailer Game',
            trailer_url='https://youtu.be/lG9PuYxh_q0?si=cv2DN1OyQVI_7FyT',
        )

        self.assertEqual(
            game.trailer_embed_url,
            'https://www.youtube.com/embed/lG9PuYxh_q0',
        )

    def test_trailer_embed_url_keeps_embed_url(self):
        game = Game(
            title='Embed Trailer Game',
            trailer_url='https://www.youtube.com/embed/pBM2xyco_Kg',
        )

        self.assertEqual(
            game.trailer_embed_url,
            'https://www.youtube.com/embed/pBM2xyco_Kg',
        )

    def test_trailer_embed_url_keeps_non_youtube_url(self):
        game = Game(
            title='External Trailer Game',
            trailer_url='https://example.com/trailer',
        )

        self.assertEqual(game.trailer_embed_url, 'https://example.com/trailer')


class GamePagesTests(TestCase):
    def _create_monthly_ratings(self, game, count, date_value):
        for index in range(count):
            user = User.objects.create(
                username=f'{game.title.lower().replace(" ", "_")}_{index}_{count}',
            )
            rating = Rating.objects.create(game=game, user=user, score=5)
            Rating.objects.filter(pk=rating.pk).update(
                created_at=date_value,
                updated_at=date_value,
            )

    def test_homepage_shows_top_three_and_top_twenty_button(self):
        now = timezone.now()
        ranking_games = [
            Game.objects.create(title='Alpha Quest'),
            Game.objects.create(title='Battle Arena'),
            Game.objects.create(title='Cyber Clash'),
            Game.objects.create(title='Dragon Fields'),
        ]

        self._create_monthly_ratings(ranking_games[0], 2, now)
        self._create_monthly_ratings(ranking_games[1], 5, now)
        self._create_monthly_ratings(ranking_games[2], 3, now)
        self._create_monthly_ratings(ranking_games[3], 1, now)

        for index in range(12):
            Game.objects.create(title=f'Random Game {index}')

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Top 3 do mês')
        top_titles = [game.title for game in response.context['top_ranked_games']]
        self.assertEqual(top_titles, ['Battle Arena', 'Cyber Clash', 'Alpha Quest'])
        self.assertTrue(response.context['show_full_ranking_link'])
        self.assertEqual(len(response.context['featured_games']), 10)

    def test_top_twenty_page_limits_results_to_twenty(self):
        now = timezone.now()

        for index in range(25):
            game = Game.objects.create(title=f'Game {index:02d}')
            self._create_monthly_ratings(game, 25 - index, now)

        response = self.client.get(reverse('monthly_ranking'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['ranking_games']), 20)
        self.assertEqual(response.context['ranking_games'][0].title, 'Game 00')
        self.assertEqual(response.context['ranking_games'][19].title, 'Game 19')

    def test_search_page_filters_results(self):
        Game.objects.create(title='The Witcher 3')
        Game.objects.create(title='Minecraft')

        response = self.client.get(reverse('game_search'), {'q': 'witcher'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Witcher 3')
        self.assertNotContains(response, 'Minecraft')

    def test_game_detail_uses_embed_url_for_youtube_trailer(self):
        game = Game.objects.create(
            title='Trailer Detail Game',
            trailer_url='https://www.youtube.com/watch?v=pBM2xyco_Kg&vl=en',
        )

        response = self.client.get(reverse('game_detail', args=[game.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'https://www.youtube.com/embed/pBM2xyco_Kg')
        self.assertNotContains(response, 'https://www.youtube.com/watch?v=pBM2xyco_Kg')

    def test_genre_page_lists_only_games_from_selected_genre(self):
        action = Genre.objects.create(name='Ação')
        puzzle = Genre.objects.create(name='Puzzle')

        first_game = Game.objects.create(title='Sky Rush')
        second_game = Game.objects.create(title='Mind Box')
        first_game.genres.add(action)
        second_game.genres.add(puzzle)

        response = self.client.get(reverse('genre_games', args=[action.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sky Rush')
        self.assertNotContains(response, 'Mind Box')

    def test_previous_month_ratings_do_not_enter_current_month_ranking(self):
        current_game = Game.objects.create(title='Modern Echo')
        old_game = Game.objects.create(title='Retro Blaze')

        self._create_monthly_ratings(current_game, 2, timezone.now())
        self._create_monthly_ratings(old_game, 4, timezone.now() - timedelta(days=40))

        response = self.client.get(reverse('monthly_ranking'))

        ranking_titles = [game.title for game in response.context['ranking_games']]
        self.assertIn('Modern Echo', ranking_titles)
        self.assertNotIn('Retro Blaze', ranking_titles)
