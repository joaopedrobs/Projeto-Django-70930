from django import forms
from .models import Estudante, Post


class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ['nome', 'sobrenome', 'email']
     

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo', 'autor', 'status']


class PesquisaEstudanteForm(forms.Form):
    termo = forms.CharField(
        label="Pesquisar estudante",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite um nome ou sobrenome'})
    )
