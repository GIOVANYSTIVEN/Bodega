from django.db import models

# Create your models here.
class Post(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.TextField()
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nombre
    