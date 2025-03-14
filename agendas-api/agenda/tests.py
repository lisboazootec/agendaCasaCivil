from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime, timedelta
import pytz
from .models import Agenda
from .serializers import AgendaSerializer

class AgendaModelTest(TestCase):
    """
    Testes para o modelo Agenda.
    """
    
    def setUp(self):
        # Configurando fuso horário para garantir consistência nos testes
        self.tz = pytz.UTC
        self.now = datetime.now(self.tz)
        
        # Criando uma agenda para testes
        self.agenda = Agenda.objects.create(
            titulo="Reunião de Equipe",
            descricao="Discutir os próximos projetos",
            dataInicio=self.now,
            dataFim=self.now + timedelta(hours=2),
            local="Sala de Conferência",
            estadoAtualAgenda="agendado"
        )
    
    def test_agenda_creation(self):
        """Teste para verificar a criação correta de uma Agenda"""
        self.assertTrue(isinstance(self.agenda, Agenda))
        self.assertEqual(self.agenda.titulo, "Reunião de Equipe")
        self.assertEqual(self.agenda.estadoAtualAgenda, "agendado")
    
    def test_agenda_str_method(self):
        """Teste para o método __str__ do modelo Agenda"""
        # Ajuste conforme a implementação do seu método __str__
        # Exemplo: se o __str__ retorna o título
        self.assertEqual(str(self.agenda), "Reunião de Equipe")
    
    def test_auto_fields(self):
        """Teste para campos automáticos (created_at, updated_at)"""
        self.assertIsNotNone(self.agenda.created_at)
        self.assertIsNotNone(self.agenda.updated_at)
        
    def test_date_validation(self):
        """Teste para validação de datas (dataFim deve ser posterior a dataInicio)"""
        # Criar agenda com dataFim anterior a dataInicio
        invalid_agenda = Agenda(
            titulo="Agenda Inválida",
            descricao="Teste de validação",
            dataInicio=self.now,
            dataFim=self.now - timedelta(hours=1),
            local="Local de Teste",
            estadoAtualAgenda="agendado"
        )
        
        # Verificar se a validação do modelo lança exceção
        # Note: Implemente esta validação no modelo se ela não existir
        with self.assertRaises(Exception):
            invalid_agenda.full_clean()


class AgendaAPITest(APITestCase):
    """
    Testes para a API de Agendas.
    """
    
    def setUp(self):
        # Limpar todas as agendas existentes antes de cada teste
        Agenda.objects.all().delete()
        
        # Configurando fuso horário
        self.tz = pytz.UTC
        self.now = datetime.now(self.tz)
        
        # Formato ISO para datas
        self.iso_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        
        # Criando algumas agendas de teste
        self.agenda1 = Agenda.objects.create(
            titulo="Reunião de Planejamento",
            descricao="Planejar próximo trimestre",
            dataInicio=self.now,
            dataFim=self.now + timedelta(hours=1),
            local="Sala 101",
            estadoAtualAgenda="agendado"
        )
        
        self.agenda2 = Agenda.objects.create(
            titulo="Entrevista de Candidato",
            descricao="Entrevista para vaga de desenvolvedor",
            dataInicio=self.now + timedelta(days=1),
            dataFim=self.now + timedelta(days=1, hours=1),
            local="Sala 202",
            estadoAtualAgenda="agendado"
        )
        
        # URL para os endpoints da API
        self.list_url = reverse('agenda-list')
        self.detail_url = reverse('agenda-detail', kwargs={'pk': self.agenda1.pk})
    
    def test_list_agendas(self):
        """Teste para listar todas as agendas"""
        # Garantir que só temos as agendas criadas no setUp
        self.assertEqual(Agenda.objects.count(), 2)
        
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Devemos ter exatamente 2 agendas
    
    def test_create_agenda(self):
        """Teste para criar uma nova agenda"""
        # Garantir que começamos com 2 agendas
        self.assertEqual(Agenda.objects.count(), 2)
        
        data = {
            'titulo': 'Nova Reunião',
            'descricao': 'Descrição da nova reunião',
            'dataInicio': (self.now + timedelta(days=2)).strftime(self.iso_format),
            'dataFim': (self.now + timedelta(days=2, hours=1)).strftime(self.iso_format),
            'local': 'Sala Virtual',
            'estadoAtualAgenda': 'agendado'
        }
        
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agenda.objects.count(), 3)
        self.assertEqual(response.data['titulo'], 'Nova Reunião')
    
    def test_retrieve_agenda(self):
        """Teste para recuperar uma agenda específica"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], self.agenda1.titulo)
    
    def test_update_agenda(self):
        """Teste para atualizar uma agenda existente"""
        data = {
            'titulo': 'Reunião Atualizada',
            'descricao': self.agenda1.descricao,
            'dataInicio': self.agenda1.dataInicio.strftime(self.iso_format),
            'dataFim': self.agenda1.dataFim.strftime(self.iso_format),
            'local': self.agenda1.local,
            'estadoAtualAgenda': self.agenda1.estadoAtualAgenda
        }
        
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.agenda1.refresh_from_db()
        self.assertEqual(self.agenda1.titulo, 'Reunião Atualizada')
    
    def test_partial_update_agenda(self):
        """Teste para atualização parcial (PATCH) de uma agenda"""
        data = {'estadoAtualAgenda': 'cancelado'}
        
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.agenda1.refresh_from_db()
        self.assertEqual(self.agenda1.estadoAtualAgenda, 'cancelado')
    
    def test_delete_agenda(self):
        """Teste para excluir uma agenda"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Agenda.objects.count(), 1)
    
    def test_create_invalid_agenda(self):
        """Teste para criar agenda com dados inválidos"""
        # Teste com data final anterior à data inicial
        data = {
            'titulo': 'Agenda Inválida',
            'descricao': 'Teste de validação',
            'dataInicio': (self.now + timedelta(days=1)).strftime(self.iso_format),
            'dataFim': self.now.strftime(self.iso_format),
            'local': 'Sala de Teste',
            'estadoAtualAgenda': 'agendado'
        }
        
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_filter_agendas_by_date(self):
        """Teste para filtrar agendas por data"""
        # Limpar todas as agendas e criar apenas as que precisamos para este teste
        Agenda.objects.all().delete()
        
        # Criar uma agenda para hoje
        agenda_hoje = Agenda.objects.create(
            titulo="Reunião Hoje",
            descricao="Descrição da reunião de hoje",
            dataInicio=self.now,
            dataFim=self.now + timedelta(hours=1),
            local="Sala 101",
            estadoAtualAgenda="agendado"
        )
        
        # Criar uma agenda para amanhã
        amanha = self.now + timedelta(days=1)
        agenda_amanha = Agenda.objects.create(
            titulo="Entrevista de Candidato",
            descricao="Entrevista para vaga de desenvolvedor",
            dataInicio=amanha,
            dataFim=amanha + timedelta(hours=1),
            local="Sala 202",
            estadoAtualAgenda="agendado"
        )
        
        # Obter a data de amanhã para o filtro
        tomorrow = amanha.strftime('%Y-%m-%d')
        
        # Fazer a requisição com o filtro
        url = f"{self.list_url}?date={tomorrow}"
        response = self.client.get(url)
        
        # Verificações
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Deve retornar apenas 1 agenda
        self.assertEqual(response.data[0]['titulo'], 'Entrevista de Candidato')


# Exemplo de implementação do filtro na ViewSet
"""
class AgendaViewSet(viewsets.ModelViewSet):
    serializer_class = AgendaSerializer
    
    def get_queryset(self):
        queryset = Agenda.objects.all()
        date = self.request.query_params.get('date', None)
        
        if date:
            # Converter para o formato correto e filtrar
            from datetime import datetime
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            queryset = queryset.filter(dataInicio__date=date_obj)
            
        return queryset
"""