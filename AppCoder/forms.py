from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.Form):

    title = forms.CharField()
    subtitle = forms.CharField()
    image = forms.ImageField()
    author = forms.CharField()
    text = forms.CharField()

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email=forms.EmailField(label='Modify E-Mail')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modify Name')
    last_name=forms.CharField(label='Modify Last Name')

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class SearchPostForm(forms.Form):
    query= forms.CharField(label='Search')
class AvatarForm(forms.Form):
    image= forms.ImageField(label="Image")