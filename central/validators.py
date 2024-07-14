import re
from validate_docbr import CPF


def nome_v (nome):
    return not nome.isnumeric()

def cpf_v (cpf_n):
    cpf = CPF()
    return cpf.validate(cpf_n)

def rg_v (rg):
    return len(rg) == 9

def tel_v (telefone):
    """Verifica se o celular respeita o formato de inserção"""
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resp = re.findall(model, telefone)
    return resp

