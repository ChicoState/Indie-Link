from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Game, Genre

class GameViewsTestCase(TestCase):
    def setUp(self):
        # Set up test data, create a user and a genre
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.genre = Genre.objects.create(name='Action')
        self.game = Game.objects.create(name='Test Game',genre = self.genre.set('Action'), description = 'test description',
                                        release_status = 'Released')
    def test_create_game_fail(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Test the create_game view
        response = self.client.post(reverse('create_game'), {'name': 'Test Game', 'genre': 'Action'})
        self.assertEqual(response.status_code, 200)  # Check if the view redirects
        self.assertFalse(Game.objects.filter(name='Test Game').exists())
    
    def test_create_game(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        test_user = User.objects.get(username='testuser')
        # Test the create_game view
        response = self.client.post(reverse('create_game'), {
            'user': test_user.id,
            'name': 'Test Game',
            'genre': ['Action'],  # Use the string value of the genre
            'description': 'Test description',
            'release_status': 'Released',
            'cover_image': r'C:\Users\shiki\Documents\GitHub\anthony\Indie-Link\indielink\media\images\apps.2884.13932426078429747.3e93ffd3-45ac-4f46-825c-e742038af698.png',  # Provide a valid image path or handle file uploads appropriately
        })
        self.assertEqual(response.status_code, 200)  # Check if the view redirects
        self.assertTrue(Game.objects.filter(name='Test Game').exists())

    def test_edit_game_view(self):
    # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Create a test game
        game = Game.objects.create(name='Test Game', user=self.user)

        # Test the edit_game view
        response = self.client.post(reverse('edit_game', args=[game.id]), {
            'name': 'Updated Game',
            'genre': [self.genre.id],
            'description': 'Updated description',
            'release_status': 'Released',
            'cover_image': 'path/to/your/updated_image.png',
        })
        self.assertEqual(response.status_code, 302)  # Check if the view redirects
        self.assertEqual(Game.objects.get(id=game.id).name, 'Updated Game')


    def test_game_list_view(self):
        # Test the game_list view
        response = self.client.get(reverse('game_list'))
        self.assertEqual(response.status_code, 302)  # Check if the view returns a successful response

    # Add more test cases for other views as needed

    def tearDown(self):
        # Clean up test data
        User.objects.all().delete()
        Genre.objects.all().delete()
        Game.objects.all().delete()