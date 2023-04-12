from django.contrib import admin
from .models import Categoria, Publicacion
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PublicacionAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Categoria)
admin.site.register(Publicacion)


