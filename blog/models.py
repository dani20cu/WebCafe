from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Título")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de Actualización")


    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    content2 = models.TextField(verbose_name="Contenido2")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    published = models.DateTimeField(default=now, verbose_name="Fecha de Publicación")
    author= models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    categories= models.ManyToManyField(Category, verbose_name="Categorias")

    created = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de Actualización")


    class Meta:
        verbose_name = "Publicacion"
        verbose_name_plural = "Publicaciones"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title
    
