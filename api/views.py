from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Carro
from .serializer import CarroSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from django.utils import timezone


class CarroListView(APIView):

    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = CarroSerializer

    def get(self, request, format=None):

        carros = Carro.objects.all()
        serializer = CarroSerializer(carros, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"mensagem": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class CarroViewSet(viewsets.ModelViewSet):

    serializer_class = CarroSerializer

    @action(detail=True, methods=['get'])
    def records(self, request, placa):

        try:
            carros = Carro.objects.filter(placa=placa)
            history = []
            for carro in carros:
                serializer = self.serializer_class(carro)
                history.append(serializer.data)

            return Response(data=history, status=status.HTTP_200_OK)

        except Carro.DoesNotExist:
            return Response("Veículo não encontrado", status=status.HTTP_404_NOT_FOUND)


    @action(detail=True, methods=['put'])
    def pay(self, request, pk):

        try:
            carro = Carro.objects.get(pk=pk)
        except Carro.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            carro.pagamento = True
            carro.save()
            return Response("Pagamento efetuado", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'])
    def out(self, request, pk):

        try:
            carro = Carro.objects.get(pk=pk)
        except Carro.DoesNotExist:
            return Response("ID não encontrado", status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            if carro.pagamento == True:
                carro.saida = timezone.now()
                tempo = (carro.saida)-(carro.entrada)
                carro.permanencia = str(int(tempo.seconds/60))+" minutos"
                carro.left = True

                carro.save()
                return Response("Saída registrada com sucesso", status=status.HTTP_200_OK)
            else:
                return Response("Pagamento pendente", status=status.HTTP_402_PAYMENT_REQUIRED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):

        try:
            carro = Carro.objects.get(pk=pk)
            carro.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
