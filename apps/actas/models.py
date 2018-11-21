from django.db import models

class Acta(models.Model):
    fechaActa = models.DateField()
    numActa = models.IntegerField()
    copActa = models.FileField(null=True, blank= True, upload_to='documents')

