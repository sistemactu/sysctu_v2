from django.db import models

# Clase de las formas de pago

class FormaPago(models.Model):
    medioPago = models.CharField(max_length = 15)

    def __str__(self):
        return self.medioPago


"""
#eliminar todas las triples comillas para que funciones como corresponde
def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        aux = datetime.now()
        filename = '{}.{}'.format(aux, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper"""
    

class Cheques(models.Model):
    serieChq = models.CharField(max_length = 60, null=True, blank=True)
    titChq = models.CharField(max_length = 60, null=True, blank=True)
    montoChq = models.IntegerField( null=True, blank=True)
    bcoChq = models.CharField(max_length = 60, null=True, blank=True)
    fchEmChq = models.DateField( null=True, blank=True)
    fchInVigChq = models.DateField( null=True, blank=True)
    fchCobChq = models.DateField(null=True, blank=True)
    copChq = models.ImageField(null=True, blank=True, upload_to="""path_and_rename("""'cehques/'""")""")
    cambioChq = models.OneToOneField('self', on_delete=models.CASCADE, null=True, blank=True)
    