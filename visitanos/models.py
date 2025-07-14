from django.db import models

class Visitanos(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="SubTítulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title 
