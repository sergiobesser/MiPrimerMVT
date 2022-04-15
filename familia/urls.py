from django.urls import path
from .views import familia

urlpatterns = [
    path('', familia, name='familia')
]
