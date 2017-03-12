from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from composer.views import home, avaliacao, historia

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^avaliacao', avaliacao, name='avaliacao'),
    url(r'^historia', historia, name='historia'),
]
