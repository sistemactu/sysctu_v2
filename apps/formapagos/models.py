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
    titChq = models.CharField(max_length = 60)
    montoChq = models.IntegerField()
    bcoChq = models.CharField(max_length = 60)
    fchEmChq = models.DateField()
    fchInVigChq = models.DateField()
    fchCobChq = models.DateField(null=True, blank=True)
    copChq = models.ImageField(null=True, blank=True, upload_to="""path_and_rename("""'cehques/'""")""")
    cambioChq = models.OneToOneField('self', on_delete=models.CASCADE, null=True, blank=True)
    