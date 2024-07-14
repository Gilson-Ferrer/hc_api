from rest_framework import viewsets, filters
from central.models import Cliente
from central.serializer import ClienteSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class ClienteViewSet (viewsets.ModelViewSet):
    ''' EXIBINDO OS ROADMAPS'''
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes =[BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf', 'email']

