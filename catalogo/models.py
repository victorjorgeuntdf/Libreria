from django.db import models

class Libro(models.Model):  
    id = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    anio_publicacion = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titulo
