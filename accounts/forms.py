from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='This will also be your username')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'password1', 'password2', )
