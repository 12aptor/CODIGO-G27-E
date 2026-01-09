from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'status')
    search_fields = ('nombre',)


admin.site.register(Producto, ProductoAdmin)