from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

from .models import Post, Avatar

# ---------- POSTS ----------
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'conteudo', 'imagem', 'status')

# ---------- USUÁRIO / PERFIL ----------
class UserRegisterForm(forms.ModelForm):
    password  = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    class Meta:
        model  = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean(self):
        dados = super().clean()
        if dados.get('password') != dados.get('password2'):
            self.add_error('password2', 'As senhas não coincidem')
        return dados

class UserUpdateForm(UserChangeForm):
    password = None
    class Meta:
        model  = User
        fields = ('email', 'first_name', 'last_name')

class CustomPasswordChangeForm(PasswordChangeForm):
    pass


# ---------- AVATAR ----------
class AvatarForm(forms.ModelForm):
    class Meta:
        model  = Avatar
        fields = ("imagem",)
