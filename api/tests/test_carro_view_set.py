from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status
from ..models import Carro
from ..views import CarroViewSet
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient


class TestCarroViewSet(TestCase):
    def setUp(self):
        self.carro = Carro.objects.create(placa="AAA-1111", permanencia="1255 minutos", entrada="2020-02-14T17:47:50.777723Z", pagamento=True, saida="2020-02-17T14:43:45.014625Z", left=True)
        self.factory = APIRequestFactory()
        self.view = CarroViewSet.as_view({'get':'records'})
        self.client = APIClient()
        self.data = {'placa': 'AAA-1111', 'permanencia': '1255 minutos', 'entrada': '2020-02-14T17:47:50.777723Z', 'pagamento': 'true', 'saida': '2020-02-17T14:43:45.014625Z', 'left':'true'}

    def test_carro_url_resolves_carro_view(self):
        view = resolve('/v1/parking/AAA-1111/')
        self.assertEquals(view.func.cls, CarroViewSet)

    def test_carro_pay_success_status_code(self):
        url = '/v1/parking/{0}/pay'.format(self.carro.pk)
        request = self.client.put(url, self.data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_carro_out_success_status_code(self):
        url = '/v1/parking/{0}/out'.format(self.carro.pk)
        request = self.client.put(url, self.data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
