from django.db import models

# Clase de las formas de pago

class FormaPago(models.Model):
    medioPago = models.CharField(max_length = 15)

    def __str__(self):
        return self.medioPago


class Cheques(models.Model):
    titChq = models.CharField(max_length = 60)
    montoChq = models.IntegerField()
    bcoChq = models.CharField(max_length = 60)
    fchEmChq = models.DateField()
    fchInVigChq = models.DateField()
    fchCobChq = models.DateField(null=True, blank=True)
    cambioChq = models.OneToOneField('self', on_delete=models.CASCADE, null=True, blank=True)
    