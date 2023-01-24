from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name = "Orden",default=0)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Fecha de edicion')

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['order','title']

    def __str__(self) -> str:
        return self.title