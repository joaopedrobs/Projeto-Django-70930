from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudante, Professor, Curso, Entrega, Post
from django.http import HttpResponse
from .forms import EstudanteForm, PostForm, PesquisaEstudanteForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages  
from django.contrib.auth import login




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


@login_required
def atualizar_post(request, id):
    post = get_object_or_404(Post, id=id)


    # Garantir que apenas o autor pode editar o post
    if post.autor != request.user:
        return redirect('lista_posts')  # Redireciona caso não seja o autor


    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)  # Não salva ainda
            post.autor = request.user  # Mantém o autor inalterado
            post.save()
            return redirect('lista_posts')  # Ajuste para a URL correta
    else:
        form = PostForm(instance=post)

    return render(request, 'AppAula/atualizar_post.html', {'form': form})


@login_required
def deletar_post(request, id):
    post = get_object_or_404(Post, id=id)
   
    if request.method == "POST":
        post.delete()
        return redirect('lista_posts')  # Redireciona de volta para a lista de posts

    return render(request, 'AppAula/confirmar_deletar_post.html', {'post': post})


class post_list_view(ListView):
    model = Post
    template_name = 'AppAula/post_list.html'  # O nome do template que vamos criar
    context_object_name = 'posts'  # O nome que será usado para acessar os posts no template
    paginate_by = 10  # Se você quiser paginar os posts


class post_detail_view(DetailView):
    model = Post
    template_name = 'AppAula/post_detail.html'  # O template que vamos criar
    context_object_name = 'post'  # O nome que será usado para acessar o post no template

class post_create_view(CreateView):
    model = Post
    form_class = PostForm  # Use o formulário que você já criou
    template_name = 'AppAula/post_form.html'  # Template para o formulário
    success_url = reverse_lazy('lista_posts_cvb')  # Redirecionar para a lista de posts após a criação


class post_update_view(UpdateView):
    model = Post
    fields = ['titulo', 'conteudo', 'status']
    template_name = 'AppAula/post_edit.html'  # Template de edição


    def get_success_url(self):
        return reverse_lazy('lista_posts_cvb')  # Redireciona para a lista de posts após a atualização
    

class post_delete_view(DeleteView):
    model = Post
    template_name = 'AppAula/post_delete.html'  # Template que perguntará se o usuário quer deletar o post
    context_object_name = 'post'  # Isso vai permitir acessar o objeto 'post' no template
    success_url = reverse_lazy('lista_posts_cvb')  # Redireciona para a lista de posts após a exclusão


def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']


            # Verifica se o nome de usuário já existe
            if User.objects.filter(username=username).exists():
                # Se o usuário já existir, mostramos uma mensagem de erro
                messages.error(request, "Este nome de usuário já está em uso. Tente outro.")
                return redirect('registro')  # Redireciona de volta para a tela de registro


            # Salvando o novo usuário
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Definindo a senha de maneira segura
            user.save()


            # Autenticando o usuário automaticamente após o registro
            login(request, user)


            # Mensagem de sucesso
            messages.success(request, "Cadastro realizado com sucesso! Você foi autenticado.")


            # Redirecionando para a página inicial ou outra página de sucesso
            return redirect('home')  # Altere 'home' para o nome de URL da sua página inicial
    else:
        form = UserRegisterForm()


    return render(request, 'AppAula/registration.html', {'form': form})