import uuid
from datetime import timedelta

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.utils.timezone import now

from users.models import EmailVerification, User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': 'Введите имя пользователя'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': 'Введите фамилию'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': 'Введите email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        valid_until = now() + timedelta(hours=24)
        record = EmailVerification.objects.create(
            user_code=uuid.uuid4(),
            user=user,
            valid_until=valid_until,
        )
        record.send_email()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control form-control-lg", 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'rounded-circle'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'image')
