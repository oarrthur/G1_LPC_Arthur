from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chamado(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    dataAbertura = models.DateField(blank=True, null=True)
    solicitante = models.ManyToManyField(User, blank=True, related_name='Solicitante')

    def __str__(self):
        return self.titulo



class Atendimento(models.Model):
    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE, blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    solicitanteAtendimento = models.ManyToManyField(User, blank=True, related_name='Solicitou')
    funcionario = models.ManyToManyField(User, blank=True, related_name='Atendente')
    STATUS_CHOICES = (
        ('Aberto', 'Aberto'),
        ('Em atendimento', 'Em atendimento'),
        ('Concluido', 'Concluído'),
        ('Cancelado', 'Cancelado')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.status






