# agendas-api/agenda/management/commands/populate_agenda.py
from django.core.management.base import BaseCommand
from agenda.models import Agenda
from faker import Faker
import random
from datetime import timedelta, datetime
from django.utils import timezone


class Command(BaseCommand):
    help = 'Populates the database with sample agenda data'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, nargs='?', default=20,
                            help='Indicates the number of agendas to be created (default: 20)')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker('pt_BR')
        Faker.seed(4321)

        self.stdout.write(self.style.SUCCESS('Deleting existing agendas...'))
        Agenda.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(f'Creating {total} new agendas...'))

        # Predefined titles (your specific events)
        predefined_titles = [
            "Reunião de Projeto",
            "Consulta Médica",
            "Reunião com Cliente",
            "Entrevista de Emprego",
            "Palestra sobre Inteligência Artificial",
            "Almoço de Equipe",
            "Reunião de Feedback",
            "Reunião de Alinhamento de Marketing",
            "Treinamento de Soft Skills",
            "Apresentação de Resultados Fiscais",
        ]

        # Function to create an agenda (to avoid code duplication)
        def create_agenda(title, start_date, duration):
            end_date = start_date + duration
            return Agenda.objects.create(
                titulo=title,
                descricao=fake.paragraph(),
                dataInicio=start_date,
                dataFim=end_date,
                local=fake.address(),
                estadoAtualAgenda=random.choice(['RECEBIDO', 'CONFIRMADO', 'CANCELADO', 'ATENDIDO']),
            )

        # Create agendas with predefined titles first, using timezone.now() + timedelta
        for i, title in enumerate(predefined_titles):
            # Consistent date generation, starting from tomorrow
            start_date = timezone.now() + timedelta(days=i + 1)
            duration = timedelta(hours=random.randint(1, 3))  # Random duration between 1 and 3 hours

            create_agenda(title, start_date, duration)
            self.stdout.write(self.style.SUCCESS(f'Created agenda: {title}'))


        # Create remaining agendas with random titles and dates
        remaining = total - len(predefined_titles)
        for _ in range(remaining):
            start_date = fake.date_time_between(start_date="-30d", end_date="+30d") # keep random dates
            duration = timedelta(hours=random.randint(1,3))

            create_agenda(fake.sentence(nb_words=6), start_date, duration)
            self.stdout.write(self.style.SUCCESS(f'Created agenda with random title.'))

        self.stdout.write(self.style.SUCCESS('Successfully populated the database.'))