from django.db import models
from tags.models import Tags
from comentarios.models import Comentario


# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(max_length=250)
    autor = models.CharField(max_length=30)
    fecha = models.DateField()
    contenido = models.TextField()


    tags = models.ManyToManyField(Tags, related_name='publicaciones')
    comentarios = models.ManyToManyField(Comentario, related_name='publicaciones')


    def __str__(self):
        return self.titulo