from django.db import models
from django.utils.timezone import now
# Create your models here.


class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    co_autor = models.CharField(max_length = 30, blank = True, null = True)# blank = True quer dizer campo não obrigatório
    data_casdatro = models.DateField(default = now)
    emprestado = models.BooleanField(default = False)
    nome_emprestado = models.CharField(max_length = 30, blank = True, null = True)
    data_emprestimo = models.DateTimeField(blank = True, null = True)
    data_devolucao = models.DateTimeField(blank = True, null = True)
    tempo_duracao = models.DateField(blank = True, null = True)

    class Meta:
        verbose_name = 'Livro'# Nome que aparece na minha página de admin do django

    def __str__(self):
        return self.nome