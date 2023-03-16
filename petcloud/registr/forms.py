from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        #fields = ('__all__')
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = (self.cleaned_data["username"])
        if commit:
            user.save()
            profile = Profile(user = user, email = user.email)
            profile.save()
        return user

