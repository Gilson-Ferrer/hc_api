import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from central.models import Cliente

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) ) 
        tel = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
        nasc = "{}/{}/{}" .format(random.randrange(1 , 29),random.randrange(1 , 12),random.randrange(1940 ,2023))
        bc = "{}" .format(random.randrange(1, 999))
        ag = "{}" .format(random.randrange(1000, 9999))
        cc = "{}-{}" .format(random.randrange(100000, 999999), random.randrange(0, 9))
        p = Cliente(nome=nome, email=email, cpf=cpf, rg=rg, tel=tel, nasc=nasc, bc=bc , ag=ag, cc=cc)
        p.save()

criando_pessoas(50)
print("Sucesso!")