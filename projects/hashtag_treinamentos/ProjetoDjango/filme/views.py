from django.shortcuts import render,redirect,reverse
from .models import Filme, Usuario
from django.views.generic import TemplateView,ListView,DetailView, FormView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin #Class que bloqueia o acesso as Views 
                                                          # Precisa ser o primeiro parametro que a view recebe 
from .forms import CriaContaForm,FormHomePage
# Create your views here.


class HomePage(FormView):
    template_name = "homepage.html"
    form_class = FormHomePage


    def get(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs) # redireciona para a homepage
    

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')

            

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


class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')


class Criarconta(FormView):
    template_name = 'criarconta.html'
    form_class = CriaContaForm


    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')


# def HomePage(request):
#     return render(request, "homepage.html")


# url - view - html
# def HomeFilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)
