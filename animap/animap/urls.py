"""animap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from animais import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        # URLs relacionadas à autenticação e gerenciamento de usuários
        path('alterar-senha/', views.alterar_senha, name='alterarSenha'),
        path('cadastro', views.cadastrar_usuario, name="cadastroUsuario"),
        path('login', views.logar_usuario, name="login"),
        path('logout', views.logoutUsuario,name="logout"),

        # URLs do painel de relatórios e páginas relacionadas
        path('painel-relatorios/', views.DashboardAnimaisView.as_view(), name='painel-relatorios'),
        path('relatorios-concluidos', views.DashboardResolvidosView.as_view(), name='relatorios_concluidos'),
        path('relatorio/', views.add_animal, name='registrar'),
        path('painel-relatorios/relatorio-animal/<uuid:pk>', views.DashboardAnimalView.as_view(), name='relatorio-animal'), 

        # Página do painel do usuário
        path('painel-usuario/', views.dashboardUser, name='painel-usuario'),

        # URL de administração do Django
        path('admin/', admin.site.urls),

        # Endpoint para a API de animais
        path('animaisApi/', views.animaisApi, name='animaisApi'),

        # Gerar relatório em PDF
        path('report/', views.gerar_relatorio, name='gerar_relatorio'),

        # Atualizar estado de um animal
        path('atualizar-estado/', views.atualizar_estado_view, name='atualizar_estado'),

        # Deletar um relatório
        path('deletar-relatorio/<int:entry_id>/', views.deletar_animal_view, name='deletar_relatorio'),

        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

