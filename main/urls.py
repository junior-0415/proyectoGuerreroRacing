"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.contrib.auth import views as auth_views

###### Importes para subir imagenes #####
from django.conf import settings
from django.conf.urls.static import static
#########################################

from main.views import inicio, inicioAdmin, logout_user, nosotros, soporte_ayuda, Error404, Error500

# handler404= Error_404.as_view()s

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    # path('loggein/', loggedIn, name='inicio-sesion'),
    path('logout/',logout_user,name='logout'),
    path('adm/', inicioAdmin, name='inicio-admin'),
    #path('login/', login.as_view(), name="login"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('nosotros/', nosotros, name='nosotros'),
    path('', include('articulos.urls')),
    path('', include('usuarios.urls')),
    path('', include('inventario.urls')),
    path('', include('facturacion.urls')),
    path('', include('django.contrib.auth.urls')),
    #path("select2/", include('django_select2.urls')),
    path('soporte-ayuda/', soporte_ayuda, name="soporte_ayuda"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404= Error404.as_view()

handler500 = Error500.as_error_view()