from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'categorias'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()
    status = models.BooleanField(default=True)
    category = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        db_column='categoria_id',
        related_name='productos',
        verbose_name='Categoría'
    )

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'productos'
