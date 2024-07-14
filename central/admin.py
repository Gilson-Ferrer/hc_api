from django.contrib import admin
from central.models import Cliente

class Clientes (admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'rg', 'email', 'nasc', 'bc', 'ag', 'cc', 'tel',)
    list_display_links = ('id', 'nome',)
    search_fields = ('nome', 'email','cpf')
    list_per_page = 20 
    ordering = ('nome',)
    
admin.site.register(Cliente, Clientes)

