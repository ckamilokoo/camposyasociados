from django.urls import path
from .views import Vregistro , iniciar_sesion , cerrar_sesion

urlpatterns = [
    path('', Vregistro.as_view(), name='login'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path('iniciar_sesion', iniciar_sesion, name='iniciar_sesion'),

]
