


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Produto
from .serializers import ProdutoSerializer
#class ProdutoViewSet(viewsets.ModelViewSet):
    #queryset = Produto.objects.all()
    #serializer_class = ProdutoSerializer
class ProdutoListCreateAPIView(APIView):
    def get(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# ProdutoSerializer está configurado para converter instâncias do modelo Produto em JSON e vice-versa, 
# permitindo a manipulação fácil dos dados na sua API.  Explicação do Código:
#Método get:
#Recupera todos os objetos Produto do banco de dados usando Produto.objects.all().
##Usa o ProdutoSerializer com many=True para serializar vários objetos.
#Retorna a resposta JSON dos produtos serializados.
#Método post:
#Recebe os dados do request e os passa para o ProdutoSerializer para validação.
##Se os dados forem válidos, o serializer chama serializer.save() para criar e salvar um novo objeto Produto.
#Retorna os dados do novo produto criado com status HTTP 201 (Created).
#Se os dados não forem válidos, retorna os erros de validação com status HTTP 400 (Bad Request).


