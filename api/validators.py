from django.core.exceptions import ValidationError
import re

def placa(value):

    if len(value) < 8 or len(value) > 8:
        raise ValidationError(('A placa deve possuir 7 caracteres'))

    if len(value) == 8:
        letras = re.findall("[a-zA-Z]", value[0:3])
        numeros = re.findall("[0-9]", value[3:8])

        if len(letras) != 3:
            raise ValidationError(
                ('Os 3 primeiros dígitos devem ser Letras, EX:XXX-0000'))
        if value[3] != '-':
            raise ValidationError(('O divisor deve ser (-)'))
        if len(numeros) != 4:
            raise ValidationError(
                ('Os 4 últimos dígitos devem ser números, EX:XXX-0000'))
