from django.contrib import admin
from django.urls import path,include
from livro.views import home 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livro/',include('livro.urls')),
    path('auth/', include('usuarios.urls')),
    path('', home),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
