from django.contrib.auth import forms
from django.contrib.auth.models import User
from django import forms

from UnisApp.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'user-input', 'placeholder': "Имя"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password-input', 'placeholder': "Пароль"}))


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'user-input', 'placeholder': "Имя"}))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'email-input', 'placeholder': "email"}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'password-input', 'placeholder': "Пароль"}))
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'password-input2', 'placeholder': "Подтвердите пароль"}))

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError('Password invalid')

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')


""" class UpdateUserForm(forms.ModelForm):
    user = forms.CharField(max_length=100,
                           required=True,
                           widget=forms.TextInput(attrs={'class': 'user_red_profile', 'placeholder': 'Имя'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'email_red_profile', 'placeholder': 'Email'}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'image-file'}))

    bio = forms.CharField(max_length=700,
                          widget=forms.Textarea(attrs={'class': 'bio_red_profile', 'placeholder': 'Расскажите о себе'}))
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'user', 'email']

 """
class EditProfileForm(forms.ModelForm):
    user = forms.CharField(max_length=100,
                           required=True,
                           widget=forms.TextInput(attrs={'class': 'user_red_profile', 'placeholder': 'Имя'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'email_red_profile', 'placeholder': 'Email'}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'image-file'}))

    bio = forms.CharField(max_length=700,
                          widget=forms.Textarea(attrs={'class': 'bio_red_profile', 'placeholder': 'Расскажите о себе'}))
    
    class Meta():
        model = User
        fields = ['first_name','last_name','username','email','password']
        
