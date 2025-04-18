from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Post(models.Model):
    class Status(models.TextChoices):
        revisao = 'R', 'Revisao'
        publicado = 'P', 'Publicado'
    titulo = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.revisao)
    subtitulo = models.CharField(max_length=200, blank=True)
    conteudo  = RichTextField()
    imagem    = models.ImageField(upload_to='posts_images/', blank=True, null=True)

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='avatares', null=True, blank=True)


    def __str__(self):
        return f"{self.user.username} - {self.imagem}"
