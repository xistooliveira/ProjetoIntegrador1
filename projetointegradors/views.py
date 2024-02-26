from django.shortcuts import render
from .models import Topic #importado do arquivo models
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request): #pega o as informaçoes e renderiza numa pagina html
    """Pagina principal do Projetointegradors"""
    return render(request, 'projetointegrador/index.html')# faz a requisição

def topics(request):
    """mostrar todos assuntos"""
    topics = Topic.objects.order_by('date_added') #recebendo banco de dados ordenados
    context = {'topics': topics}#chave,valor
    return render(request, 'projetointegrador/topics.html', context) #faz requisição do servidor
def home(request):
    return render(request, 'projetointegrador/home.html')

def topic(request, topic_id):
    """mostra um unico assunto a todas suas entradas"""
    topic = Topic.objects.get(id = topic_id)#pega a informação do banco dados
    entries = topic.entry_set.order_by('-date_added')#entradas relacionadas a topic serao ordenadas.
    context = {'topic': topic, 'entries': entries} #recebe dicionario duas chaves;topic e todas relacionadas a topic.
    return render(request, 'projetointegrador/topic.html', context)
def new_topic(request):
    """adiciona um novo assunto"""
    if request.method != 'POST':
        #nenhm dado submetido; cria um formulario em branco
        form = TopicForm() #variavel  recebe funcao da classe TopicForm que foi importado do nosso arquivo
    else: 
        # Dados de POST submetidos; processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():#se os dados nao form verdadeiro nao salva
            form.save()#salva altomaticamente usando model no banco de dados
            return HttpResponseRedirect(reverse('topics'))#vc pode redirecionar para outra pagina(http)
    context = {'form': form}
    return render(request, 'projetointegrador/new_topic.html', context)
