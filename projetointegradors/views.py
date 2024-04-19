from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry, Produto, Saida, ItemSaida #importado do arquivo models
from .forms import TopicForm, EntryForm, ProdutoForm, SaidaForm, ItemSaidaForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required#permite so quem estiver logado ter acesso as viwes
# Create your views here.
def index(request): #pega o as informaçoes e renderiza numa pagina html
    """Pagina principal do Projetointegradors"""
    return render(request, 'projetointegrador/index.html')# faz a requisição

#def home(request):
  #  return render(request, 'projetointegrador/home.html')  #


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




@login_required#RESTRICAO DA PAGINA
def lista_produtos(request):
    #primeira busca de produtos
    produtos = Produto.objects.all()
    #retornamos o template p/ lista de produtos
    return render(request, 'projetointegrador/lista_produtos.html', {'produtos' : produtos})

@login_required#RESTRICAO DA PAGINA
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


#def editar_produto(id_produto, novo_nome, nova_categoria, novo_codigo, novo_existente, novo_sku, novo_preco, nova_quantidade):
   # try:
       # produto = Produto.objects.get(id=id_produto)

        # Atualize os campos conforme necessário
       # produto.nome = novo_nome
       # produto.categoria = nova_categoria
        #produto.codigo = novo_codigo
        #produto.existente = novo_existente
        #produto.sku = novo_sku
        #produto.preco = novo_preco
       # produto.quantidade = nova_quantidade

        # Salve as alterações no banco de dados
       # produto.save()

        #return "Produto editado com sucesso."

    #except Produto.DoesNotExist:
        #return "Produto não encontrado."

# Exemplo de uso:
# editar_produto(1, "Novo Nome", "Nova Categoria", "Novo Código", True, "Novo SKU", 19.99, 50)
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'projetointegrador/editar_produto.html', {'form': form, 'produto': produto})



def lista_saida(request):
    saidas = Saida.objects.all()
    return render(request, 'projetointegrador/lista_saida.html', {'saidas': saidas})

def adicionar_saida(request):
    if request.method == 'POST':
        form = SaidaForm(request.POST)
        if form.is_valid():
            saida = form.save()
            return redirect('detalhes_saida', pk=saida.pk)
    else:
        form = SaidaForm()
    return render(request, 'projetointegrador/form_saida.html', {'form': form})

def detalhes_saida(request, pk):
    saida = Saida.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemSaidaForm(request.POST)
        if form.is_valid():
            item_saida = form.save(commit=False)
            item_saida.saida = saida
            item_saida.save()
            return redirect('detalhes_saida', pk=pk)
    else:
        form = ItemSaidaForm()
    return render(request, 'projetointegrador/detalhes_saida.html', {'saida': saida, 'form': form})


def registrar_saida(request):
    produtos_disponiveis = Produto.objects.filter(existente=True, quantidade__gt=0)
    if request.method == 'POST':
        form = SaidaForm(request.POST)
        if form.is_valid():
            nova_saida = form.save()  # Salvar a saída
            
            # Processar cada item da saída
            for produto_id, quantidade in request.POST.items():
                if produto_id.startswith('produto_'):
                    produto_id = produto_id.replace('produto_', '')
                    produto = get_object_or_404(Produto, pk=produto_id)

                    
                    quantidade = int(quantidade)
                    if quantidade > 0 and produto.quantidade >= quantidade:
                        ItemSaida.objects.create(saida=nova_saida, produto=produto, quantidade=quantidade)
                        produto.quantidade -= quantidade
                        produto.save()

            return redirect('lista_produtos')  # Redirecionar para a lista de produtos após a saída ser registrada

    else:
        form = SaidaForm()

    return render(request, 'projetointegrador/form_saida.html', {'form': form, 'produtos_disponiveis': produtos_disponiveis})


@login_required
def remover_saida(request, saida_id):
    # Obtenha a saída pelo ID (ou retorne um erro 404 se não existir)
    saida = get_object_or_404(Saida, pk=saida_id)

    if request.method == 'POST':
        # Deletar a saída e todos os seus itens associados
        itens_saida = ItemSaida.objects.filter(saida=saida)
        for item in itens_saida:
            # Restaurar a quantidade do produto associado ao item
            item.produto.quantidade += item.quantidade
            item.produto.save()

        # Deletar a saída (e todos os seus itens associados) do banco de dados
        saida.delete()

        return redirect('lista_saida')  # Redirecionar para a lista de saídas após remover a saída

    return render(request, 'projetointegrador/remover_saida.html', {'saida': saida})