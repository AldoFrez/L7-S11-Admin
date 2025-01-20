from django.db import models

class Energia(models.Model):
    nivel_nombre = models.CharField(max_length=100)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return self.nivel_nombre

# Create your models here.
