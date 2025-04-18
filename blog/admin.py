from django.contrib import admin
from .models import Post, Avatar

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ("titulo", "autor", "data_publicacao", "slug")
    list_filter   = ("autor", "data_publicacao")
    search_fields = ("titulo", "subtitulo")

@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ("user", "imagem")
