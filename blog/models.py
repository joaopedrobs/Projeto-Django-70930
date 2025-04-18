from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    class Status(models.TextChoices):
        REVISÃO   = 'R', 'Revisão'
        PUBLICADO = 'P', 'Publicado'

    titulo           = models.CharField(max_length=200)
    subtitulo        = models.CharField(max_length=200, blank=True)
    conteudo         = RichTextField()
    imagem           = models.ImageField(upload_to='posts_images/', blank=True, null=True)
    status           = models.CharField(
                          max_length=1,
                          choices=Status.choices,
                          default=Status.REVISÃO,
                      )
    slug             = models.SlugField(max_length=80, unique=True, blank=True)
    data_publicacao  = models.DateTimeField(auto_now_add=True)
    autor            = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-data_publicacao']

    def save(self, *args, **kwargs):
        # gera slug automático (assegura unicidade)
        if not self.slug:
            base = slugify(self.titulo)
            slug = base
            n = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})



class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='avatares', null=True, blank=True)


    def __str__(self):
        return f"{self.user.username} - {self.imagem}"
