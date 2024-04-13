from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView,ListView,DetailView

# Create your views here.


class HomePage(TemplateView):
    template_name = "homepage.html"



class HomeFilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    # object_list

class DetalhesFilme(DetailView):
    template_name = "detalhesfilme.html"
    model =  Filme

    def get_context_data(self, **kwargs):
        context = super(DetalhesFilme, self).get_context_data(**kwargs)
        # filtrar a minha tabela de filmes pegando os filmes cuja categoria é igual a categoria do filme da página (object)
        # self.get_object() == filme
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context




# def HomePage(request):
#     return render(request, "homepage.html")


# url - view - html
# def HomeFilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)
