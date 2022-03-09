from django.contrib import admin
from django.db import models
from .models import CategoriaItem, Item, Feedback

class Admin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'cidade', 'contato', 'valor', 'data')

class FeedAdmin(admin.ModelAdmin):
    list_display = ('user', 'motivo')    
    

admin.site.register(CategoriaItem)
admin.site.register(Item, Admin)
admin.site.register(Feedback, FeedAdmin)
    
