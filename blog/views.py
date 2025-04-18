from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Post, Avatar
from .forms import (
    PostForm, UserRegisterForm, UserUpdateForm,
    CustomPasswordChangeForm, AvatarForm,
)

from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView,
    TemplateView,
)


# ---------- BLOG ----------

class HomeView(ListView):
    """Mostra os 3 posts mais recentes na página inicial"""
    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    queryset = Post.objects.order_by("-data_publicacao")[:3]

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"
    paginate_by = 6
    ordering = ["-data_publicacao"]

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
    slug_field = "slug"            
    slug_url_kwarg = "slug"        


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "post_form.html"
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "post_form.html"
    success_url = reverse_lazy("posts")

    def test_func(self):
        return self.get_object().autor == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy("posts")

    def test_func(self):
        return self.get_object().autor == self.request.user


# ---------- AUTH / PERFIL ----------

def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "registration.html", {"form": form})

@login_required
def perfil(request):
    return render(request, "perfil.html", {"user": request.user})

@login_required
def editar_perfil(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Perfil atualizado!")
            return redirect("perfil")
    else:
        user_form = UserUpdateForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)
    return render(
        request,
        "editar_perfil.html",
        {"user_form": user_form, "password_form": password_form},
    )

@login_required
def upload_avatar(request):
    avatar, _ = Avatar.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            form.save()
            return redirect("perfil")
    else:
        form = AvatarForm(instance=avatar)
    return render(request, "upload_avatar.html", {"form": form})

# ---------- SOBRE ----------

class AboutView(TemplateView):
    template_name = "about.html"
