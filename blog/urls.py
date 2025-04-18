from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    HomeView, PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    registro, perfil, editar_perfil, upload_avatar,
    AboutView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    # --- BLOG ---
    path("posts/",                 PostListView.as_view(),   name="posts"),
    path("posts/novo/",            PostCreateView.as_view(), name="post_create"),
    path("posts/<slug:slug>/",     PostDetailView.as_view(), name="post_detail"),  # ← aqui
    path("posts/<int:pk>/editar/", PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/excluir/",PostDeleteView.as_view(), name="post_delete"),

    # /pages/ deve apontar para a mesma lista
    path("pages/",  PostListView.as_view(),   name="pages_list"),
    path("pages/<int:pk>/", PostDetailView.as_view(), name="pages_detail"),

    # --- AUTENTICAÇÃO & PERFIL ---
    path("registro/",      registro,                       name="registro"),
    path("login/",         auth_views.LoginView.as_view(), name="login"),
    path("logout/",        auth_views.LogoutView.as_view(),name="logout"),
    path("perfil/",        perfil,                         name="perfil"),
    path("editar-perfil/", editar_perfil,                  name="editar_perfil"),
    path("editar-avatar/", upload_avatar,                  name="editar_avatar"),

    # --- SOBRE ---
    path("about/", AboutView.as_view(), name="about"),
]
