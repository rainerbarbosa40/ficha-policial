from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 
from .views import index, adicionar_ficha, editar_ficha

urlpatterns = [
     path('', views.index, name='index'),
     path('adicionar_ficha/', views.adicionar_ficha, name='adicionar_ficha'),
    path('editar_ficha/<int:matr>/', editar_ficha, name='editar_ficha'),
]

# Adicione esta linha para servir arquivos estáticos durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
