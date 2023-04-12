from django.shortcuts import render
from blog.models import Publicacion , Categoria

# Create your views here.
def blog(request):
    publicaciones=Publicacion.objects.all()

    return render(request, "blog/blog.html", {"publicaciones":publicaciones})

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    publicaciones=Publicacion.objects.filter(categorias=categoria)
    return render (request , "blog/categorias.html",{'categoria':categoria,"publicaciones":publicaciones})