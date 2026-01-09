from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'productos'