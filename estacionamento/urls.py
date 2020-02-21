from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/', include(('api.urls', 'api'), namespace='api')),
]
