from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry, Produto #importado do arquivo models
from .forms import TopicForm, EntryForm, ProdutoForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required#permite so quem estiver logado ter acesso as viwes
# Create your views here.
def index(request): #pega o as informaçoes e renderiza numa pagina html
    """Pagina principal do Projetointegradors"""
    return render(request, 'projetointegrador/index.html')# faz a requisição

@login_required#RESTRICAO DA PAGINA
def topics(request):
    """mostrar todos assuntos"""
    topics = Topic.objects.order_by('date_added') #recebendo banco de dados ordenados
    context = {'topics': topics}#chave,valor
    return render(request, 'projetointegrador/topics.html', context) #faz requisição do servidor
def home(request):
    return render(request, 'projetointegrador/home.html')

@login_required#RESTRICAO DA PAGINA
def topic(request, topic_id):
    """mostra um unico assunto a todas suas entradas"""
    topic = Topic.objects.get(id = topic_id)#pega a informação do banco dados
    entries = topic.entry_set.order_by('-date_added')#entradas relacionadas a topic serao ordenadas.
    context = {'topic': topic, 'entries': entries} #recebe dicionario duas chaves;topic e todas relacionadas a topic.
    return render(request, 'projetointegrador/topic.html', context)

@login_required#RESTRICAO DA PAGINA
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
            return HttpResponseRedirect(reverse('topic'))#vc pode redirecionar para outra pagina(http)
    context = {'form': form}
    return render(request, 'projetointegrador/new_topic.html', context)

@login_required#RESTRICAO DA PAGINA
def new_entry(request, topic_id):
    """acrescenta uma nova entrada """
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        #nenhm dado submetido; cria um formulario em branco
        form = EntryForm() #variavel  recebe funcao da classe TopicForm que foi importado do nosso arquivo
    else: 
        # Dados de POST submetidos; processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():#se os dados nao form verdadeiro nao salva
           new_entry = form.save(commit=False)#salva altomaticamente usando model no banco de dados
           new_entry.topic = topic
           new_entry.save()
           return HttpResponseRedirect(reverse('topic', args=[topic_id]))#vc
    context = {'topic':topic, 'form':form} #recebe dicionario duas chaves;topic e todas relacionadas a topic.
    return render(request, 'projetointegrador/new_entry.html', context)

def edit_entry(request, entry_id):
    """edita uma entrada existente"""
    entry = Entry.objects.get(id=entry_id)#pegua o objeto pelo id
    topic = entry.topic

    if request.method != 'POST':
    #requesicao inicial; prenche previamente com a entrada atual.
        form = EntryForm(instance=entry)
    else: 
    # dados de POST submetidos, processa os dados
        form = EntryForm(instance=entry, data=request.POST)#substitui os dados pelo que ja estava
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[entry_id]))#argumentos exigido por topic
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'projetointegrador/edit_entry.html', context)





def lista_produtos(request):
    #primeira busca de produtos
    produtos = Produto.objects.all()
    #retornamos o template p/ lista de produtos
    return render(request, 'projetointegrador/lista_produtos.html', {'produtos' : produtos})


def cria_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
            
    return render(request, 'projetointegrador/cria_produto.html', {'form' : form})
def remove_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produto.delete()
    return redirect('lista_produtos')
