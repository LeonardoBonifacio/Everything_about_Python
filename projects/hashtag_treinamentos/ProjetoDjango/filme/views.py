from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView,ListView

# Create your views here.


class HomePage(TemplateView):
    template_name = "homepage.html"



class HomeFilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    # object_list




# def HomePage(request):
#     return render(request, "homepage.html")


# url - view - html
# def HomeFilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)
