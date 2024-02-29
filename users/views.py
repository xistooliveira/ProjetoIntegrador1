#from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect 
from django.urls import reverse
from django.contrib.auth import logout

def logout_view(request):
    """faz um logout do usuario"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))#redireciona a pagina para index
