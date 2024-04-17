from django.shortcuts import render,redirect
from .models import Filme
from django.views.generic import TemplateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin #Class que bloqueia o acesso as Views 
                                                          # Precisa ser o primeiro parametro que a view recebe 

# Create your views here.


class HomePage(TemplateView):
    template_name = "homepage.html"


    def get(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs) # redireciona para a homepage
            

class HomeFilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme
    # object_list

class DetalhesFilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model =  Filme

    def get(self,request, *args, **kwargs):
        # descobrir qual filme ele esta acessando
        # somar 1 nas visualizações daquele filmes
        # salvar
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save() # salva as alterações feitas no banco de dados
        usuario = request.user
        usuario.filmes_vistos.add(filme) 
        return super().get(request, *args, **kwargs) # redirecionao o usuário para a url final

    def get_context_data(self, **kwargs):
        context = super(DetalhesFilme, self).get_context_data(**kwargs)
        # filtrar a minha tabela de filmes pegando os filmes cuja categoria é igual a categoria do filme da página (object)
        # self.get_object() == filme
        filmes_relacionados = self.model.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context


class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains = termo_pesquisa)
            return object_list
        else:
            return None


class Paginaperfil(LoginRequiredMixin, TemplateView):
    template_name = 'editarperfil.html'




# def HomePage(request):
#     return render(request, "homepage.html")


# url - view - html
# def HomeFilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)
