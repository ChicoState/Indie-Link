from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Game, Genre, GameImage, Comment, DevPost
from .views import edit_game, genre_search
from .forms import CommentForm, DevPostForm, GenreSearchForm

class GameViewsTestCase(TestCase):
    def setUp(self):
        # Set up test data, create a user and a genre
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.genre = Genre.objects.create(name='Action')
        #self.game = Game.objects.create(name='Test Game',genre = self.genre.set('Action'), description = 'test description',
        #                                release_status = 'Released')
        self.game = Game.objects.create(
            user=self.user,
            name='Test Game',
            description='Test description',
            release_status='In Development',
            cover_image='path/to/your/image.png'
        )
        self.game.genre.add(self.genre)

        self.game_image = GameImage.objects.create(game=self.game, game_image='path/to/your/game_image.png')
    
    def test_create_game_fail(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Test the create_game view
        response = self.client.post(reverse('create_game'), {'name': 'Cool Game', 'genre': 'Action'})
        self.assertEqual(response.status_code, 200)  # Check if the view redirects
        self.assertFalse(Game.objects.filter(name='Cool Game').exists())
    
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
        # Test the edit_game view
        response = self.client.post(reverse('edit_game', args=[self.game.id]), {
            'name': 'Updated Game',
            'description': 'Updated description',
            'release_status': 'Released',
        })
        self.assertEqual(response.status_code, 200)  # Check if the view redirects

    def test_genre_search_view(self):
        self.client.login(username='testuser', password='testpassword')

        # Create a test genre
        # Send a POST request to the genre_search view
        response = self.client.post(reverse('search'), {'genre': self.genre.id, 'search': 'Search'})

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the rendered page contains details of the search results
        self.assertContains(response, 'Action')
        self.assertContains(response, 'Test Game')

    def test_game_list_view(self):
        # Test the game_list view
        response = self.client.get(reverse('game_list'))
        self.assertEqual(response.status_code, 302)  # Check if the view returns a successful response

    def test_game_detail_view_authenticated_user(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Send a GET request to the game_detail view
        response = self.client.get(reverse('game_detail', args=[self.game.id]))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the rendered page contains the game details
        self.assertContains(response, 'Test Game')
        self.assertContains(response, 'Test description')

        # Check if the rendered page contains the game image
        self.assertContains(response, 'path/to/your/game_image.png')

        # Check if the rendered page contains the comment form
        self.assertIsInstance(response.context['form'], CommentForm)


    def test_delete_games_view(self):
        self.client.login(username='testuser', password='testpassword')
        # Send a POST request to the delete_games view
        response = self.client.post(reverse('delete_games'))

        # Check if the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check if the games and associated images are deleted
        self.assertFalse(Game.objects.filter(user=self.user).exists())
        self.assertFalse(GameImage.objects.filter(game__user=self.user).exists())

        # Check if the redirect goes to 'game_list'
        self.assertRedirects(response, reverse('game_list'))

    def test_add_fav_view(self):
        self.client.login(username='testuser', password='testpassword')
        # Send a POST request to the add_fav view
        response = self.client.post(reverse('add_fav', args=[self.game.id]))

        # Check if the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check if the game is added to the user's favorites
        self.assertTrue(self.user.favorite.filter(id=self.game.id).exists())

        # Check if the redirect goes to 'game_detail'
        self.assertRedirects(response, reverse('game_detail', args=[self.game.id]))


    def test_remove_fav_view(self):
        self.client.login(username='testuser', password='testpassword')
        # Add the game to the user's favorites
        self.user.favorite.add(self.game)
        # Send a POST request to the remove_fav view
        response = self.client.post(reverse('remove_fav', args=[self.game.id]))

        # Check if the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check if the game is removed from the user's favorites
        self.assertFalse(self.user.favorite.filter(id=self.game.id).exists())

        # Check if the redirect goes to 'game_detail'
        self.assertRedirects(response, reverse('game_detail', args=[self.game.id]))

    def test_create_dev_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        # Send a POST request to the create_dev_post view
        response = self.client.post(reverse('create_dev_post', args=[self.game.id]), {
            'title': 'Test Dev Post',
            'content': 'Test content for the dev post',
        })

        # Check if the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check if a DevPost object is created for the game
        self.assertTrue(DevPost.objects.filter(game=self.game, title='Test Dev Post').exists())

        # Check if the redirect goes to 'game_detail'
        self.assertRedirects(response, reverse('game_detail', args=[self.game.id]))

    def test_create_dev_post_view_invalid_form(self):
        self.client.login(username='testuser', password='testpassword')

        # Send a POST request with invalid form data to the create_dev_post view
        response = self.client.post(reverse('create_dev_post', args=[self.game.id]), {
            'title': '',  # Invalid data to trigger form validation error
            'content': 'Test content for the dev post',
        })

        # Check if the response status code is 200 (OK) when form is invalid
        self.assertEqual(response.status_code, 200)

        # Check if the DevPost object is not created for the game
        self.assertFalse(DevPost.objects.filter(game=self.game, title='Test Dev Post').exists())


    def test_edit_dev_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        self.dev_post = DevPost.objects.create(game=self.game, title='Test Dev Post', content='Test content')
        # Send a POST request to the edit_dev_post view
        response = self.client.post(reverse('edit_dev_post', args=[self.game.id, self.dev_post.id]), {
            'title': 'Updated Dev Post',
            'content': 'Updated content for the dev post',
        })

        # Check if the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check if the DevPost object is updated
        self.dev_post.refresh_from_db()
        self.assertEqual(self.dev_post.title, 'Updated Dev Post')

        # Check if the redirect goes to 'game_detail'
        self.assertRedirects(response, reverse('game_detail', args=[self.game.id]))

    def test_edit_dev_post_view_invalid_form(self):
        self.client.login(username='testuser', password='testpassword')
        self.dev_post = DevPost.objects.create(game=self.game, title='Test Dev Post', content='Test content')
        # Send a POST request with invalid form data to the edit_dev_post view
        response = self.client.post(reverse('edit_dev_post', args=[self.game.id, self.dev_post.id]), {
            'title': '',  # Invalid data to trigger form validation error
            'content': 'Updated content for the dev post',
        })

        # Check if the response status code is 200 (OK) when form is invalid
        self.assertEqual(response.status_code, 200)

        # Check if the DevPost object is not updated
        self.dev_post.refresh_from_db()
        self.assertNotEqual(self.dev_post.title, '')

    def test_dev_post_detail_view(self):
        self.client.login(username='testuser', password='testpassword')
        self.dev_post = DevPost.objects.create(game=self.game, title='Test Dev Post', content='Test content')

        # Send a GET request to the dev_post_detail view
        response = self.client.get(reverse('dev_post_detail', args=[self.game.id, self.dev_post.id]))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the rendered page contains the game and dev post details
        self.assertContains(response, 'Test Dev Post')
        self.assertContains(response, 'Test content')



    def tearDown(self):
        # Clean up test data
        User.objects.all().delete()
        Genre.objects.all().delete()
        Game.objects.all().delete()
        GameImage.objects.all().delete()
        Comment.objects.all().delete()