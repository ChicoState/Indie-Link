from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create your tests here.
class GameFormTest(LiveServerTestCase):

    def test_a_login(self):
        selenium = webdriver.Edge()

        # Opening the links we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        username = selenium.find_element(By.ID,'id_username')
        password = selenium.find_element(By.ID,'id_password')

        login = selenium.find_element(By.ID,'login')

        username.send_keys('user')
        password.send_keys('user')

        login.send_keys(Keys.RETURN)

        # Find the profile link
        profile_link = selenium.find_element(By.XPATH,"//a[@href='profile/']")
        profile_link.click()

        # Check the returned result
        assert 'Welcome, user!' in selenium.page_source

    def test_b_logout(self):
        selenium = webdriver.Edge()

        # Opening the links we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        username = selenium.find_element(By.ID,'id_username')
        password = selenium.find_element(By.ID,'id_password')

        login = selenium.find_element(By.ID,'login')

        username.send_keys('user')
        password.send_keys('user')

        login.send_keys(Keys.RETURN)

        # Find the logout link
        logout_link = selenium.find_element(By.XPATH,"//a[@href='/logout/']")
        logout_link.click()

        # Check the returned result
        assert 'Login' in selenium.page_source

    def test_c_create_game(self):
        selenium = webdriver.Edge()

        # Opening the links we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        username = selenium.find_element(By.ID,'id_username')
        password = selenium.find_element(By.ID,'id_password')

        login = selenium.find_element(By.ID,'login')

        username.send_keys('user')
        password.send_keys('user')

        login.send_keys(Keys.RETURN)

        selenium.get('http://127.0.0.1:8000/create_game/')

        # Find the form elements
        game_name = selenium.find_element(By.ID,'id_name')
        game_description = selenium.find_element(By.ID,'id_description')
        game_release_status = selenium.find_element(By.ID,'id_release_status')
        game_cover_image = selenium.find_element(By.ID,'id_cover_image')

        game_submit = selenium.find_element(By.ID,'submit')

        # Fill the form with data
        game_name.send_keys('Test Game')
        game_description.send_keys('This is a test game')
        game_release_status.send_keys('Released')
        game_cover_image.send_keys('C:/Users/jared/Downloads/test.jpg')
        
        # Submitting the form
        game_submit.send_keys(Keys.RETURN)

        # Check the returned result
        assert 'Test Game' in selenium.page_source

    def test_d_edit_game(self):
        selenium = webdriver.Edge()

        # Opening the links we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        username = selenium.find_element(By.ID,'id_username')
        password = selenium.find_element(By.ID,'id_password')

        login = selenium.find_element(By.ID,'login')

        username.send_keys('user')
        password.send_keys('user')

        login.send_keys(Keys.RETURN)

        selenium.get('http://127.0.0.1:8000/game_list/')

        # Find the details button
        details_button = selenium.find_element(By.NAME,"details")
        details_button.click()

        # Find the edit button
        edit_button = selenium.find_element(By.NAME, "edit")
        edit_button.click()

        # Find the form elements
        game_name = selenium.find_element(By.ID,'id_name')
        game_description = selenium.find_element(By.ID,'id_description')
        game_release_status = selenium.find_element(By.ID,'id_release_status')
        game_cover_image = selenium.find_element(By.ID,'id_cover_image')

        game_submit = selenium.find_element(By.ID,'submit')

        # Fill the form with data
        game_name.clear()
        game_name.send_keys('Edit Test')
        game_description.clear()
        game_description.send_keys('This is a test to edit the game')
        game_release_status.send_keys('In Development')
        game_cover_image.clear()
        game_cover_image.send_keys('C:/Users/jared/Downloads/test.jpg')

        # Submitting the form
        game_submit.send_keys(Keys.RETURN)

        # Check the returned result
        assert 'Edit Test' in selenium.page_source

    def test_e_add_favorite(self):
        selenium = webdriver.Edge()

        # Opening the links we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        username = selenium.find_element(By.ID,'id_username')
        password = selenium.find_element(By.ID,'id_password')

        login = selenium.find_element(By.ID,'login')

        username.send_keys('user')
        password.send_keys('user')

        login.send_keys(Keys.RETURN)

        selenium.get('http://127.0.0.1:8000/game_list/')

        # Find the details button
        details_button = selenium.find_element(By.NAME,"details")
        details_button.click()

        # Find the favorite button
        favorite_button = selenium.find_element(By.NAME,"fav")
        favorite_button.click()

        # Find the home button
        home_button = selenium.find_element(By.NAME,"home")
        home_button.click()

        # Find the favorite link
        favorites_link = selenium.find_element(By.XPATH,"//a[@href='favorites/']")
        favorites_link.click()

        # Check the returned result
        assert 'Edit Test' in selenium.page_source

    def test_f_remove_favorite(self):
        selenium = webdriver.Edge()

        # Opening the links we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        username = selenium.find_element(By.ID,'id_username')
        password = selenium.find_element(By.ID,'id_password')

        login = selenium.find_element(By.ID,'login')

        username.send_keys('user')
        password.send_keys('user')

        login.send_keys(Keys.RETURN)

        selenium.get('http://127.0.0.1:8000/game_list/')

        # Find the details button
        details_button = selenium.find_element(By.NAME,"details")
        details_button.click()

        # Find the favorite button
        remove_favorite_button = selenium.find_element(By.NAME,"rem")
        remove_favorite_button.click()

        # Find the home button
        home_button = selenium.find_element(By.NAME,"home")
        home_button.click()

        # Find the favorite link
        favorites_link = selenium.find_element(By.XPATH,"//a[@href='favorites/']")
        favorites_link.click()

        # Check the returned result
        assert 'Edit Test' not in selenium.page_source

    def test_g_create_dev_post(self):
        selenium = webdriver.Edge()

        # Opening the links we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        username = selenium.find_element(By.ID,'id_username')
        password = selenium.find_element(By.ID,'id_password')

        login = selenium.find_element(By.ID,'login')

        username.send_keys('user')
        password.send_keys('user')

        login.send_keys(Keys.RETURN)

        selenium.get('http://127.0.0.1:8000/game_list/')

        # Find the details button
        details_button = selenium.find_element(By.NAME,"details")
        details_button.click()

        # Find the create dev post button
        create_dev_post_button = selenium.find_element(By.NAME,"dev")
        create_dev_post_button.click()

        # Find the form elements
        dev_post_title = selenium.find_element(By.ID,'id_title')
        dev_post_content = selenium.find_element(By.ID,'id_content')

        dev_post_submit = selenium.find_element(By.NAME,"dev_post")

        # Fill the form with data
        dev_post_title.send_keys('Test Dev Post')
        dev_post_content.send_keys('This is a test dev post')

        # Submitting the form
        dev_post_submit.send_keys(Keys.RETURN)

        # Check the returned result
        assert 'Development Blog' in selenium.page_source and 'Test Dev Post' in selenium.page_source

    def test_z_delete_game(self):
        selenium = webdriver.Edge()

        # Opening the links we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        username = selenium.find_element(By.ID,'id_username')
        password = selenium.find_element(By.ID,'id_password')

        login = selenium.find_element(By.ID,'login')

        username.send_keys('user')
        password.send_keys('user')

        login.send_keys(Keys.RETURN)

        selenium.get('http://127.0.0.1:8000/game_list/')

        # Find the delete button
        delete = selenium.find_element(By.ID,'delete')
        delete.send_keys(Keys.RETURN)

        # Check the returned result
        assert 'Edit Test' not in selenium.page_source
