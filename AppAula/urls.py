from django.urls import include, path
from .views import lista_estudantes, detalhe_estudante, lista_posts, detalhe_post, criar_estudante, criar_post, pesquisa_estudante


urlpatterns = [
    path('estudantes/', lista_estudantes, name='lista_estudantes'),
    path('estudantes/<int:pk>/', detalhe_estudante, name='detalhe_estudante'),
    path('post/', lista_posts, name='lista_posts'),  
    path('post/<int:post_id>/', detalhe_post, name='detalhe_post'),
    path('estudantes/criar/', criar_estudante, name='criar_estudante'),
    path('posts/criar/', criar_post, name='criar_post'),
    path('pesquisa-estudante/', pesquisa_estudante, name='pesquisa_estudante'),

]


