from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AccountsAuthTests(TestCase):
    def test_register_creates_user_and_logs_in(self):
        response = self.client.post(reverse('register'), {
            'username': 'arthur',
            'email': 'arthur@example.com',
            'password1': 'SenhaForte123',
            'password2': 'SenhaForte123',
        })

        self.assertRedirects(response, reverse('home'))
        user = User.objects.get(username='arthur')
        self.assertEqual(self.client.session.get('_auth_user_id'), str(user.id))

    def test_login_with_valid_credentials(self):
        user = User.objects.create_user(username='arthur', password='SenhaForte123')

        response = self.client.post(reverse('login'), {
            'username': 'arthur',
            'password': 'SenhaForte123',
        })

        self.assertRedirects(response, reverse('home'))
        self.assertEqual(self.client.session.get('_auth_user_id'), str(user.id))

    def test_login_with_invalid_credentials_shows_error(self):
        User.objects.create_user(username='arthur', password='SenhaForte123')

        response = self.client.post(reverse('login'), {
            'username': 'arthur',
            'password': 'senha-errada',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Usuário ou senha incorretos.')

    def test_logout_clears_session(self):
        user = User.objects.create_user(username='arthur', password='SenhaForte123')
        self.client.force_login(user)

        response = self.client.get(reverse('logout'))

        self.assertRedirects(response, reverse('login'))
        self.assertNotIn('_auth_user_id', self.client.session)
