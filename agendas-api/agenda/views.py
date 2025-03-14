from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Agenda
from .serializers import AgendaSerializer
from drf_yasg.utils import swagger_auto_schema  # Correct
from django.db.models import Q
from django.utils import timezone # Import timezone

class AgendaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar e editar agendas.
    """
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

    @swagger_auto_schema(
        operation_description="Lista todas as agendas disponíveis",
        responses={200: AgendaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retorna os detalhes de uma agenda específica",
        responses={
            200: AgendaSerializer(),
            404: "Agenda não encontrada"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Cria uma nova agenda, garantindo que as datas estejam corretas",
        request_body=AgendaSerializer,
        responses={
            201: AgendaSerializer(),
            400: "Dados inválidos"
        }
    )
    def create(self, request, *args, **kwargs):
        """
        Cria uma nova agenda, garantindo que as datas estejam corretas.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(
        operation_description="Permite atualização completa de uma agenda",
        request_body=AgendaSerializer,
        responses={
            200: AgendaSerializer(),
            400: "Dados inválidos",
            404: "Agenda não encontrada"
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Permite atualização parcial, incluindo o estado da agenda",
        request_body=AgendaSerializer(partial=True),
        responses={
            200: AgendaSerializer(),
            400: "Dados inválidos",
            404: "Agenda não encontrada"
        }
    )
    def partial_update(self, request, *args, **kwargs):
        """
        Permite atualização parcial, incluindo o estado da agenda.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Remove uma agenda",
        responses={
            204: "Agenda removida com sucesso",
            404: "Agenda não encontrada"
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Agenda.objects.all()
        date_str = self.request.query_params.get('date', None)
        if date_str:
            try:
                # Use timezone.make_aware to handle timezones correctly
                date_obj = timezone.datetime.strptime(date_str, '%Y-%m-%d').date()
                aware_datetime = timezone.make_aware(timezone.datetime.combine(date_obj, timezone.datetime.min.time()))
                queryset = queryset.filter(
                    Q(dataInicio__date=aware_datetime.date()) |
                    Q(dataFim__date=aware_datetime.date())
                )
            except ValueError:
                pass  # Ignore invalid date formats
        return queryset