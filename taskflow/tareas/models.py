from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Etiqueta(models.Model):
    tipo = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.tipo

class Post(models.Model):
    TZ = [
        ("Pendiente", "Pendiente"),
        ("En Progreso", "En Progreso"),
        ("Completada", "Completada"),
    ]
    title = models.CharField(max_length=100, verbose_name='Titulo del Posteo')
    content = models.TextField(verbose_name='Contenido del Posteo', max_length=256, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author del Posteo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion del Post')
    tzone = models.CharField(choices=TZ, verbose_name='Estado', max_length=20, default='Pendiente')
    observations = models.TextField(verbose_name='Observaciones', blank=True, null=True)
    etiqueta_tarea = models.ForeignKey(Etiqueta, default=1,on_delete=models.CASCADE)
    fecha_limite = models.DateTimeField( verbose_name='Fecha Limite del Post')

    def __str__(self):
        return self.title + ' - ' + str(self.created_at)