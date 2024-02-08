from account.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "email-form",
        "placeholder": "Enter username",
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "password-form",
        "placeholder": "Enter password",
    }))


class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'})

    )


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = 'new-password'
        self.fields['new_password2'].widget.attrs['class'] = 'new-password-confirmation'
        self.fields['new_password1'].widget.attrs['placeholder'] = "New Password"
        self.fields['new_password2'].widget.attrs['placeholder'] = 'New Password Confirmation'
