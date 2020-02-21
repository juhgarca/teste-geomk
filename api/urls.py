from django.conf.urls import url
from .views import CarroListView, CarroViewSet

urlpatterns = [
    url(r'^parking/?$', CarroListView.as_view(), name='parking'),
    url(r'^parking/(?P<placa>\w{3}-\d{4})/?$', CarroViewSet.as_view({'get':'records'}), name='records'),
    url(r'^parking/(?P<pk>[0-9]+)/pay/?$', CarroViewSet.as_view({'put':'pay'}), name='pay'),
    url(r'^parking/(?P<pk>[0-9]+)/out/?$', CarroViewSet.as_view({'put':'out'}), name='out'),
]
