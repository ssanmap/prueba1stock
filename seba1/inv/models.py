from django.db import models

# Create your models here.

class stock(models.Model):
    title = models.CharField ( max_length=150 )
    medida = models.CharField ( max_length=100 )
    price = models.IntegerField ()
    pricesale = models.IntegerField ()
    cantidad = models.IntegerField ()
    fechaElab = models.DateTimeField ()
    FechaExp = models.DateTimeField ()
    Estado = models.IntegerField ()

    def __str__(self):
        return self.title