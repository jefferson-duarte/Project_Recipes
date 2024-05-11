from .base import AuthorsBaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.mark.functional_test
class AuthorsRegisterTest(AuthorsBaseTest):

    def fill_form_dummy_data(self, form):
        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 20)

    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/main/div[2]/form'
        )

    def form_field_test_with_callback(self, callback):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        self.fill_form_dummy_data(form)
        form.find_element(By.NAME, 'email').send_keys('dummy@email.com')

        callback(form)
        return form

    def test_empty_first_name_error_message(self):
        def calback(form):
            first_name_field = self.get_by_placeholder(form, 'Ex.: John')
            first_name_field.send_keys(' ')
            first_name_field.send_keys(Keys.ENTER)

            form = self.get_form()

            self.assertIn('Write your first name', form.text)
        self.form_field_test_with_callback(calback)

    def test_empty_last_name_error_message(self):
        def calback(form):
            last_name_field = self.get_by_placeholder(form, 'Ex.: Doe')
            last_name_field.send_keys(' ')
            last_name_field.send_keys(Keys.ENTER)

            form = self.get_form()

            self.assertIn('Write your last name', form.text)
        self.form_field_test_with_callback(calback)

    def test_empty_username_error_message(self):
        def calback(form):
            username_field = self.get_by_placeholder(form, 'Your username')
            username_field.send_keys(' ')
            username_field.send_keys(Keys.ENTER)

            form = self.get_form()

            self.assertIn('This field must not be empty', form.text)
        self.form_field_test_with_callback(calback)

    def test_invalid_email_error_message(self):
        def calback(form):
            email_field = self.get_by_placeholder(form, 'Your email')
            email_field.send_keys('email@invalid')
            email_field.send_keys(Keys.ENTER)

            form = self.get_form()

            self.assertIn('The e-mail must be valid', form.text)
        self.form_field_test_with_callback(calback)

    def test_password_do_not_match(self):
        def calback(form):
            password1 = self.get_by_placeholder(form, 'Type your password')
            password2 = self.get_by_placeholder(form, 'Repeat your password')
            password1.send_keys('P@ssword')
            password2.send_keys('P@ssword_Different')
            password2.send_keys(Keys.ENTER)

            form = self.get_form()

            self.assertIn('Password and password2 must be equal', form.text)
        self.form_field_test_with_callback(calback)

    def test_user_valid_data_register_successfully(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        self.get_by_placeholder(form, 'Ex.: John').send_keys('First Name')
        self.get_by_placeholder(form, 'Ex.: Doe').send_keys('Last Name')
        self.get_by_placeholder(form, 'Your username').send_keys('my_username')
        self.get_by_placeholder(
            form, 'Your email').send_keys('email@valid.com')
        self.get_by_placeholder(
            form, 'Type your password').send_keys('P@ssw0rd1')
        self.get_by_placeholder(
            form, 'Repeat your password').send_keys('P@ssw0rd1')

        form.submit()

        self.assertIn(
            'Your user is created, please lon in.',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
