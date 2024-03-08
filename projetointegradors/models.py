from django.db import models

# Create your models here.
class Topic(models.Model): #topico tabela no banco de dados
    text = models.CharField(max_length=200)#define quant max de caracteres
    date_added = models.DateTimeField(auto_now_add=True)#herda de models e define horario p/ os dados

    def __str__(self):#define o painel admin, devolve uma representacao do modelo
        """devolve uma representacao """
        return self.text
class Entry(models.Model):#entrando com informacoes para classe Topic
    """algo espefico aprendido (esta em models)"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)#chave estrangeira para Topic erdar este modelo relacional
    #esta topic on_delete para que nao apague todo o topico use nulo
    text = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True)#erda de models e define horario p/ os dados
class Meta:
    verbose_name_plural = 'entries' #regra de ingles no plural de Entry
def __str__(self):
    """devolve uma string do modelo"""
    return self.text[50] + '...' #quantidade de caracteres


class Produto(models.Model):
    categoria = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    codigo = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        unique=True)
    existente = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    sku = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        unique=True
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False
    )
    quantidade = models.IntegerField()

def __str__(self):
    return self.name


    
