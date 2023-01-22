from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='Nombre')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Fecha de edicion')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name="Fecha de publicación",default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog",null=True,blank=True)
    author = models.ForeignKey(User,verbose_name="Autor",on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category,verbose_name="Categorias")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Fecha de edicion')

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created_at']