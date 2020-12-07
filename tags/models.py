from django.db import models



# Create your models here.
class Tags(models.Model) :
    nombre = models.CharField('Nombre Clase', max_length=80)
    def __str__(self):
        return self.nombre