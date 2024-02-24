from django.shortcuts import render

# Create your views here.
def index(request): #pega o as informaçoes e renderiza numa pagina html
    """Pagina principal do Projetointegradors"""
    return render(request, 'projetointegrador/index.html')