from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='This will also be your username')
    methods = forms.BooleanField(required=False)
    physics = forms.BooleanField(required=False)
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['methods'].label = "Access methods videos?"
        self.fields['physics'].label = "Access physics videos?"

    class Meta:
        model = User
        fields = ('email', 'first_name', 'password1', 'password2', 'methods', 'physics',)
