from . import views 
from django.urls import path

urlpatterns = [
    path('', views.produtoList, name='produto-list'),
    path('produto_detalhe/<int:id>', views.produtoDetalhe, name='produto-detalhe'),
]