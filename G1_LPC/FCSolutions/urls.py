from django.contrib import admin
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^todos', todosChamados, name='todos'),
    url(r'^chamados/usuario/(?P<pk>[0-9]+)', chamadoID, name='chamadoID'),
    url(r'^atendimentos/concluidos', atendimentosConcluidos, name='atendimentosConcluidos')
]