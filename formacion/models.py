from django.db import models

# Create your models here.

class Formacion(models.Model):
    imagen = models.ImageField(upload_to = 'formacion')
    titulo = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    objetivo_th1 = models.CharField(max_length= 50)
    habilidAdq_th2 = models.CharField(max_length= 50)
    td = models.JSONField()
    competencias = models.CharField(max_length=50)
    li = models.JSONField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'formacion'
        verbose_name_plural = 'formaciones'

    def __str__(self):
        return self.titulo
    
