from django.db import models
from django.utils.timezone import now
from usuarios.models import Usuario
# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    co_autor = models.CharField(max_length = 30, blank = True, null = True)# blank = True quer dizer campo não obrigatório
    data_cadastro = models.DateField(default = now)
    emprestado = models.BooleanField(default = False)
    nome_emprestado = models.CharField(max_length = 30, blank = True, null = True)
    data_emprestimo = models.DateTimeField(blank = True, null = True)
    data_devolucao = models.DateTimeField(blank = True, null = True)
    tempo_duracao = models.DateField(blank = True, null = True)
    categoria = models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Livro'# Nome que aparece na minha página de admin do django

    def __str__(self):
        return self.nome