from django.contrib import admin
from .models import Post, Avatar   # só o que existe

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "data_publicacao", "status")
    list_filter  = ("status", "data_publicacao")
    search_fields = ("titulo", "conteudo")
    ordering = ("-data_publicacao",)

@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ("user",)
