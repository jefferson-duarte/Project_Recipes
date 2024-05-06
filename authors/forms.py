import re
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
            code='Invalid'
        )


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your email')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['password'], 'Type your password')
        add_placeholder(self.fields['password2'], 'Reapet your password')

    username = forms.CharField(
        label='Username',
        help_text=(
            'Username must have letters, numbers or one of those @.+-_. '
            'The length should be between 4 and 150 characters.'
        ),
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Username must have at least 4 characters',
            'max_length': 'Username must have less than 150 characters',
        },
        min_length=4,
        max_length=150,
    )

    first_name = forms.CharField(
        error_messages={'required': 'Write your first name'},
        label='First name'
    )

    last_name = forms.CharField(
        error_messages={'required': 'Write your last name'},
        label='Last name'
    )

    email = forms.EmailField(
        error_messages={
            'required': 'E-mail is required',
        },
        label='E-mail',
        help_text='The e-mail must be valid'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
        validators=[
            strong_password
        ],
        label='Password'
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Password2',
        error_messages={
            'required': 'Please, reapet your password',
        },
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password': 'Password and password2 must be equal.',
                'password2': 'Password and password2 must be equal.'
            })
