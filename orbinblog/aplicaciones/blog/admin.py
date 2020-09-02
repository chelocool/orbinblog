from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CategoriaResource(resources.ModelResource):
    class Meta:
        model=Categoria

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields=['nombre']
    list_display=('nombre', 'estado', 'fecha_creacion',)
    resource_class=CategoriaResource

class AutorResoruce(resources.ModelResource):
    class Meta:
        model=Autor

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_field=['nombres', 'apellidos', 'correo']
    list_display=('nombres', 'apellidos', 'correo' , 'estado', 'fecha_creacion')
    resources_class=AutorResoruce

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)    
