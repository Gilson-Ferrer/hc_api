from rest_framework import serializers
from central.models import Cliente
from central.validators import *
class ClienteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def validate(self,data):
        
        if not nome_v (data['nome']):
            raise serializers.ValidationError({"nome": "Não inserir números"})
        if not cpf_v (data['cpf']):
            raise serializers.ValidationError({"cpf": "Digite um CPF válido"})
        if not rg_v (data['rg']):
            raise serializers.ValidationError({"rg": "RG deverá conter 9 dígitos"})
        if not tel_v (data['tel']):
            raise serializers.ValidationError({"tel": "Insira o Telefone conforme exemplo 11 98765-4321 (deverá conter espaço e o traço)"})
        
        return data
        
        
