
from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudante, Professor, Curso, Entrega, Post
from django.http import HttpResponse
from .forms import EstudanteForm, PostForm, PesquisaEstudanteForm

def index(request):
    return HttpResponse("Olá, bem vindo ao APP Aula!")


def lista_estudantes(request):
    estudantes = Estudante.objects.all()
    return render(request, 'AppAula/estudantes_list.html', {'estudantes': estudantes})


def detalhe_estudante(request, pk):
    estudante = get_object_or_404(Estudante, pk=pk)
    return render(request, 'AppAula/estudante_detail.html', {'estudante': estudante})


def lista_posts(request):
    posts = Post.objects.all().order_by('-data_publicacao')
    return render(request, 'AppAula/lista_posts.html', {'posts': posts})


def detalhe_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'AppAula/detalhe_post.html', {'post': post})



def criar_estudante(request):
    if request.method == 'POST':
        form = EstudanteForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o estudante no banco de dados
            return redirect('lista_estudantes')  # Redireciona para a lista de estudantes
    else:
        form = EstudanteForm()
        return render(request, 'AppAula/criar_estudante.html', {'form': form})


def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo post no banco de dados
            return redirect('lista_posts')  # Redireciona para a página de lista de posts
    else:
        form = PostForm()
    return render(request, 'AppAula/criar_post.html', {'form': form})


def pesquisa_estudante(request):
    resultados = None
    form = PesquisaEstudanteForm(request.GET)  
    if form.is_valid():
        termo = form.cleaned_data.get('termo')
        if termo:
            resultados = Estudante.objects.filter(
                nome__icontains=termo
            ) | Estudante.objects.filter(
                sobrenome__icontains=termo
            )
    return render(request, 'AppAula/pesquisa_estudante.html', {'form': form, 'resultados': resultados})