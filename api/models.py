from django.db import models
from .validators import placa
from django.utils import timezone

def get_date():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

class Carro(models.Model):

    def __str__(self):
        return str(self.placa)

    placa = models.CharField(max_length=8, validators=[placa], verbose_name='Placa')
    permanencia = models.CharField(max_length=21, default='0 minutos', verbose_name='Permanência')
    entrada = models.DateTimeField(default=timezone.now(), verbose_name='Entrada')
    pagamento = models.BooleanField(default=False, verbose_name='Pagamento')
    saida = models.DateTimeField(default='2019-01-01T00:00:00.000000Z', verbose_name='Saída')
    left = models.BooleanField(default=False, verbose_name='Left')

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
