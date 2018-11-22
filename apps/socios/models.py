from django.db import models
from apps.formapagos.models import FormaPago
from apps.actas.models import Acta


#clase representativa del socio del club con toda la informacion personal del mismo
class Socio(models.Model):
    nombCompSoc = models.CharField(max_length=70)#nombre completo del socio
    rutSoc = models.CharField(max_length=10)#rut del socio
    domicSoc = models.CharField(max_length=100)#domicilio particular del socio
    fecNacSoc = models.DateField(null=True)#fecha de nacimiento del socio
    mailSoc = models.EmailField(null=True, blank=True)#correo electronico
    celSoc = models.CharField(max_length= 12, null=True, blank=True)#telefono del socio
    telSoc = models.CharField(max_length=12, null=True, blank=True)#telefono de la oficina
    profecSoc = models.CharField(max_length=30, null=True, blank=True)#profecion socio
    trabSoc = models.CharField(max_length=30, null=True, blank=True)#trabajo socio
    edadSoc = models.IntegerField(null=True, blank=True)#edad del socio
    nacionalidadSoc = models.CharField(max_length=30)#nacionalidad del socio
    estCivSoc = models.CharField(max_length=10)#estado civil
    conySoc = models.CharField(max_length=70, null=True, blank=True)#conyuge si es que tiene
    numHijMenSoc = models.IntegerField( null=True, blank=True)#numero de hijos menores de edad
    poctSoc = models.CharField(max_length=50, null=True, blank=True)#pertenecia a otros club de tenis
    ocsSoc = models.CharField(max_length=50, null=True, blank=True)#pertenencia a otros clubs sociales
    catTenSoc = models.CharField(max_length=50, null=True, blank=True)#categoria tenistica
    numCas = models.CharField(max_length=50, null=True, blank=True)#numero de casillero
    cuotInc = models.IntegerField(null=True, blank=True)#cuota de incorporacion
    cuotSoc = models.IntegerField(null=True, blank=True)#cuota social
    totPag = models.IntegerField(null=True, blank=True)#total del pago
    formPaInsc = models.ForeignKey(FormaPago, on_delete=models.CASCADE, null=True, blank=True)#forma de pago de la inscripcion
    tipoSoc = models.CharField(max_length=50, null=True, blank=True)#tipo de socio
    socPatr = models.ForeignKey('self' , on_delete=models.CASCADE, null=True, related_name='+', blank=True)#socio patrocinador
    primSocFe = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='+', blank=True)#socio que conoce al postulante
    secSocFe = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='+', blank=True)#segundo socio que conoce al postulante
    fecSolic =  models.DateField(null=True, blank=True)#fecha de solicitud
    estSolic = models.CharField(max_length=1, null=True, blank=True)#estado de la solicitud valores posibles p=pendiente r=rechazada a=aceptada
    fecAcept = models.DateField(null=True, blank=True)#fecha de aceptacion del 
    acta = models.ForeignKey(Acta, on_delete=models.CASCADE, null=True, blank=True)#referencia al acta de resolucion
    infSolic = models.TextField(null=True, blank=True)#informe final
    fotoSoc = models.ImageField(null=True, blank=True)#foto del socio



