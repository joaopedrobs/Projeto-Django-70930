from django import forms
from .models import Estudante, Post, Professor, Curso


class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ['nome', 'sobrenome', 'email']
     

class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ["titulo", "conteudo", "autor"]   # status = default 'draft'
        widgets = {
            "conteudo": forms.Textarea(attrs={"rows": 4}),
        }



class PesquisaEstudanteForm(forms.Form):
    termo = forms.CharField(
        label="Pesquisar estudante",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite um nome ou sobrenome'})
    )

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ["nome", "sobrenome", "email", "profissao"]

class CursoForm(forms.ModelForm):
    class Meta:
        model  = Curso
        fields = ["nome", "turma"]