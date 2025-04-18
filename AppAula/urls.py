from django.urls import include, path
from .views import lista_estudantes, detalhe_estudante, lista_posts, detalhe_post, criar_estudante, criar_post, pesquisa_estudante, atualizar_post, deletar_post
from .views import post_list_view, post_detail_view, post_create_view, post_update_view, post_delete_view, registro

urlpatterns = [
    path('estudantes/', lista_estudantes, name='lista_estudantes'),
    path('estudantes/<int:pk>/', detalhe_estudante, name='detalhe_estudante'),
    path('post/', lista_posts, name='lista_posts'),  
    path('post/<int:post_id>/', detalhe_post, name='detalhe_post'),
    path('estudantes/criar/', criar_estudante, name='criar_estudante'),
    path('posts/criar/', criar_post, name='criar_post'),
    path('pesquisa-estudante/', pesquisa_estudante, name='pesquisa_estudante'),
    path('post/editar/<int:id>/', atualizar_post, name='atualizar_post'),
    path('post/deletar/<int:id>/', deletar_post, name='deletar_post'),
    path('posts/', post_list_view.as_view(), name='lista_posts_cvb'),
    path('post/<int:pk>/', post_detail_view.as_view(), name='detalhe_post_cvb'),
    path('post/criar/', post_create_view.as_view(), name='criar_post_cvb'),
    path('post/editar/<int:pk>/', post_update_view.as_view(), name='atualizar_post_cvb'),
    path('deletar/<int:pk>/', post_delete_view.as_view(), name='deletar_post_cvb'),
    path('registro/', registro, name='registro'),

]
