from django.db import models

# Create your models here.
class Comentario(models.Model):
    autor = models.CharField(max_length=30)
    fecha = models.DateField()
    email = models.EmailField(max_length=50)
    puntos = models.IntegerField()
    contenido = models.TextField()


    def __str__(self) :
        return self.autor

