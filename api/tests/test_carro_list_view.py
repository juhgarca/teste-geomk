from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from rest_framework import status
from ..views import CarroListView
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

class TestCarroListView(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CarroListView.as_view()
        self.client = APIClient()
        self.data = {'placa': 'AAA-1111', 'permanencia': '1255 minutos', 'entrada': '2020-02-14T17:47:50.777723Z', 'pagamento': 'true', 'saida': '2020-02-17T14:43:45.014625Z', 'left':'true'}

    def test_carros_view_success_status_code(self):
        url = reverse('api:parking')
        request = self.factory.get(url)
        response = self.view(request)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_carros_url_resolves_view(self):
        view = resolve('/v1/parking/')
        self.assertEquals(view.func.view_class, CarroListView)

    def test_carros_post_success_status_code(self):
        url = reverse('api:parking')
        request = self.client.post(url, self.data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_carros_post_failure_status_code(self):
        url = reverse('api:parking')
        request = self.client.post(url)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
