from django.db import models   # traz as ferramentas para criar tabelas


class Livro(models.Model):     # classe no SINGULAR = vira a tabela core_livro no banco
    # texto curto (VARCHAR 200)
    titulo = models.CharField(max_length=200)
    # texto curto (VARCHAR 150)
    autor = models.CharField(max_length=150)
    ano = models.IntegerField()                        # número inteiro (INT)
    # texto curto (VARCHAR 100)
    genero = models.CharField(max_length=100)
    # dinheiro: até 10 dígitos, 2 casas decimais
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    url_imagem = models.URLField(
        max_length=500, blank=True, null=True)  # link da capa, OPCIONAL

    def __str__(self):         # como o livro aparece quando é "impresso" (ex: no admin)
        return self.titulo
