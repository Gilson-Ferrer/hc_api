from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9)
    email = models.EmailField(max_length=100)
    nasc = models.CharField(max_length=10)
    bc = models.CharField(max_length=20, default='')
    ag = models.CharField(max_length=25, default='')
    cc = models.CharField(max_length=25, default='')
    tel = models.CharField(max_length=13)

    def __str__(self):
        return self.nome
    

    
    