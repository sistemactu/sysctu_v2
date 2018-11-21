from django.db import models
import os
from datetime import datetime


"""
def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        aux = datetime.now()
        filename = '{}.{}'.format(aux, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper"""


class Acta(models.Model):



    fechaActa = models.DateField()
    numActa = models.IntegerField()
    copActa = models.FileField(null=True, blank=True, upload_to='documents/')
