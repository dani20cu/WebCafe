from django.db import models

# Create your models here.
class Social(models.Model):
    key = models.SlugField(max_length=200, verbose_name="Nombre clave", null=True, blank=True, unique=True)
    name = models.CharField(max_length=200, verbose_name="Social Name")
    url = models.URLField(verbose_name="Enlace URL", max_length=200, null=True, blank=True)
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Sociales"
        ordering = ["-created"]
    
    def __str__(self):
        return self.name