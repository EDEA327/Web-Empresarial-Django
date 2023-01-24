from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Fecha de edicion')

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['title']

    def __str__(self) -> str:
        return self.title