from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField('Nombre de la Categoria', max_length=100, null=False, blank=False)
    estado=models.BooleanField('Categoria Activada/Categoria no Activada', default=True)
    fecha_creacion=models.DateTimeField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    id=models.AutoField(primary_key=True)
    nombres=models.CharField('Nombre', max_length=50, null=False, blank=False)
    apellidos=models.CharField('Apellido', max_length=50, null=False, blank=False)
    web=models.URLField('Web', null=False, blank=True)
    correo=models.EmailField('Correo', null=False, blank=True)
    estado=models.BooleanField('Activo/No Activo', default=True)
    fecha_creacion=models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True) 


    class Meta:
        verbose_name='Autor'
        verbose_name_plural='Autores'

    def __str__(self):
        return "{0}, {1}".format(self.apellidos, self.nombres)


class Post(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField('Titulo', max_length=100, null=False, blank=False)
    slug=models.CharField('Slug', max_length=100, null=False, blank=False)
    descipcion=models.CharField('Descripcion', max_length=200, null=False, blank=False)
    contenido=RichTextField()
    imagen=models.URLField(max_length=200, null=False, blank=False)
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado=models.BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion=models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
        

    def __str__(self):
        return self.titulo