from rest_framework import serializers
from .models import Carro

class CarroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carro
        fields = ('id', 'placa', 'permanencia', 'entrada', 'pagamento', 'saida', 'left')
