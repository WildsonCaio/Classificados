from django import forms
from django.forms import widgets
from django.forms.widgets import Widget 
from .models import Feedback, Item, CategoriaItem

class Task(forms.ModelForm):
    class Meta:
        city = [('Soure','Soure'),
                ('Salvaterra','Salvaterra')]
        model = Item
        fields = ['titulo', 'categoria', 'valor', 'descricao', 'cidade', 'bairro', 'foto',
                  'foto2', 'foto3', 'contato', 'contato2']
        widgets = {
            'cidade': forms.Select(choices=city),
        }

class Task2(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['motivo', 'descricao',]
        

        