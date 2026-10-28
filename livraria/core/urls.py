from django.urls import path, include               # ferramentas de rota
from rest_framework.routers import DefaultRouter    # gera as rotas do CRUD sozinho
# a view que acabamos de criar
from .views import LivroViewSet

# cria o "gerador de rotas"
router = DefaultRouter()
# tudo em /livros/ vai para o LivroViewSet
router.register('livros', LivroViewSet, basename='livro')

urlpatterns = [
    # entrega as rotas geradas ao Django
    path('', include(router.urls)),
]
