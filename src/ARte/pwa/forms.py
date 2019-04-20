from django import forms
from django.contrib.auth import get_user_model

from .models import Exhibition


User = get_user_model()

class ExhibitionForm(forms.ModelForm):
    
    class Meta:
        model = Exhibition
        fields = ['name']


class UploadFileForm(forms.Form):
    file = forms.ImageField(required=False)


class SignupForm(forms.ModelForm):
    """
    Form for new users registration.
    """
    password = password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput,
        help_text='Your password'
    )
    password_confirm = password = forms.CharField(
        label='Password confirmation',
        required=True,
        widget=forms.PasswordInput,
        help_text='Confirm your password'
    )

    class Meta:
        model = User
        fields = ['name', 'email']

    def _post_clean(self):
        super()._post_clean()
        data = self.cleaned_data
        if data.get('password') != data.get('password_confirm'):
            self.add_error('password_confirm', 'Passwords do not match')


class LoginForm(forms.Form):
    """
    User login.
    """
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput,
        help_text='Your password'
    )
