from django.test import TestCase 
from django.urls import reverse, resolve 

from api.views import CarroListView, CarroViewSet 
 
class ParkingUrlsTestCase(TestCase): 
 
    def test_resolves_list_url(self): 
        resolver = self.resolve_by_name('get') 
         
        self.assertEqual(resolver.func.cls, CarroListView) 

