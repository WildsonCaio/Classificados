from django.db import models
from django.contrib.auth.models import User

class CategoriaItem(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tudo')
    titulo    = models.CharField(max_length=30)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(CategoriaItem, on_delete=models.CASCADE, blank=False)
    foto      = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/')
    foto2     = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/')
    foto3     = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/')
    cidade    = models.CharField(max_length=30)
    bairro    = models.CharField(max_length=30)
    contato   = models.CharField(max_length=20)
    contato2  = models.CharField(max_length=20, blank=True)
    valor     = models.CharField(max_length=20)
    data      = models.CharField(max_length=8, blank=True)
    ativo     = models.BooleanField(default=True)
    def __str__(self):
        return self.titulo
    
    
class Feedback(models.Model):
    option = [
        ('Sugestâo', 'Sugestão'),
        ('Reclamação', 'Reclamação'),
        ('Parceria', 'Parceria'),
        ('Outro','Outro')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    motivo    = models.CharField(max_length=10, choices=option)
    descricao = models.TextField()
    def __str__(self):
        return self.motivo