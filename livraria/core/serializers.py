from rest_framework import serializers   # ferramentas de conversão do DRF
# o ponto (.) = "da mesma pasta" (core)
from .models import Livro


class LivroSerializer(serializers.ModelSerializer):   # "tradutor" Livro <-> JSON
    class Meta:                  # configurações do tradutor
        model = Livro            # qual tabela ele traduz
        fields = '__all__'       # traduz TODAS as colunas (id incluso)
