from django.shortcuts import render, get_object_or_404
from .models import Produto, Categoria
from django.core.paginator import Paginator

# Create your views here.
def produtoList(request):

    filtro = request.GET.get('filter')
    search = request.GET.get('search')

    if search:
        produtos_lista = Produto.objects.filter(nome__icontains=search) 
    elif filtro:
        produtos_lista = Produto.objects.filter(categoria=filtro) 
    else:
        produtos_lista = Produto.objects.all() 
    
    categorias =  Categoria.objects.all()
    paginator = Paginator(produtos_lista,6) 
    page = request.GET.get('page')

    produtos = paginator.get_page(page)

    return render(request,'lista_produtos.html',{'produtos':produtos,'categorias':categorias})


def produtoDetalhe(request,id):
    produto = get_object_or_404(Produto,pk=id)
    return render(request,'produto_detalhes.html',{'produto':produto})

