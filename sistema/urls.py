from django.contrib import admin
from django.urls import path
from sistema.views import lista_obras  # se o seu app tiver outro nome, troque 'sistema' pelo nome dele

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_obras, name='lista_obras'),
]