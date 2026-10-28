# traz o ViewSet (CRUD automático)
from rest_framework import viewsets
# @action = cria endpoints extras
from rest_framework.decorators import action
from rest_framework.response import Response         # devolve a resposta em JSON
from .models import Livro                            # a tabela
from .serializers import LivroSerializer             # o tradutor JSON


# ModelViewSet = GET, POST, PUT, PATCH, DELETE prontos
class LivroViewSet(viewsets.ModelViewSet):
    # de onde vêm os dados: todos os livros
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer               # quem traduz para JSON

    # GET /api/livros/autor/Tolkien/
    @action(detail=False, methods=['get'], url_path='autor/(?P<nome>[^/.]+)')
    def por_autor(self, request, nome=None):
        # autor CONTÉM o texto (ignora maiúsc/minúsc)
        livros = self.queryset.filter(autor__icontains=nome)
        # many=True = é uma LISTA de livros
        serializer = self.get_serializer(livros, many=True)
        # devolve o JSON
        return Response(serializer.data)

    # GET /api/livros/ano/1954/
    @action(detail=False, methods=['get'], url_path='ano/(?P<ano>[0-9]+)')
    def por_ano(self, request, ano=None):
        # ano EXATAMENTE igual
        livros = self.queryset.filter(ano=ano)
        serializer = self.get_serializer(livros, many=True)
        return Response(serializer.data)

    # GET /api/livros/genero/Fantasia/
    @action(detail=False, methods=['get'], url_path='genero/(?P<genero>[^/.]+)')
    def por_genero(self, request, genero=None):
        livros = self.queryset.filter(
            genero__icontains=genero)  # gênero CONTÉM o texto
        serializer = self.get_serializer(livros, many=True)
        return Response(serializer.data)

    # GET /api/livros/titulo/Duna/
    @action(detail=False, methods=['get'], url_path='titulo/(?P<titulo>[^/.]+)')
    def por_titulo(self, request, titulo=None):
        livros = self.queryset.filter(
            titulo__icontains=titulo)  # título CONTÉM o texto
        serializer = self.get_serializer(livros, many=True)
        return Response(serializer.data)
