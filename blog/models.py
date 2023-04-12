from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)

    class meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__(self):
        return self.nombre


class Publicacion(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='publicaciones', null=True , blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)
   

    class meta:
        verbose_name='publicacion'
        verbose_name_plural='publicaciones'
    
    def __str__(self):
        return self.titulo    