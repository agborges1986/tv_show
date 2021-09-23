from django.db import models

# Create your models here.

class Show(models.Model):
    titulo=models.TextField(max_length=80)
    productor= models.TextField(max_length=80)
    lanzamiento=models.DateTimeField()
    descripcion=models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
