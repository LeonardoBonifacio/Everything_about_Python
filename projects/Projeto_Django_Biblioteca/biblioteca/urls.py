from django.contrib import admin
from django.urls import path,include
from livro.views import home 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('livro/',include('livro.urls')),
    path('auth/', include('usuarios.urls')),
    path('', home),
]
