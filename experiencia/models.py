from django.db import models

# Create your models here.
class Experiencia(models.Model):
    imagen = models.ImageField(upload_to = 'experiencia')
    empresa = models.CharField(max_length=50)
    periodo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    habilidadesCom = models.CharField(max_length=50)
    td = models.JSONField()
    habilidAdq = models.CharField(max_length=50)
    li = models.JSONField()
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now_add=True)
    # class Meta:
    #     verbose_name = 'experiencia'
    #     verbose_name_plural = 'experiencias'

    # def __str__(self):
    #     return self.empresa