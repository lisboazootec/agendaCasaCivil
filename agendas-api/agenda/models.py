from django.db import models
from django.utils import timezone  # Import timezone
from django.core.exceptions import ValidationError

class Agenda(models.Model):
    ESTADO_CHOICES = (
        ('RECEBIDO', 'Recebido'),
        ('CONFIRMADO', 'Confirmado'),
        ('CANCELADO', 'Cancelado'),
        ('ATENDIDO', 'Atendido'),
    )

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    dataInicio = models.DateTimeField()  # No changes needed here
    dataFim = models.DateTimeField()    # No changes needed here
    local = models.CharField(max_length=200, blank=True, null=True)
    estadoAtualAgenda = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='RECEBIDO'
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Correct
    updated_at = models.DateTimeField(auto_now=True)      # Correct

    class Meta:
        ordering = ['dataInicio']

    def __str__(self):
        return self.titulo

    def clean(self):
        """
        Valida que a data de fim é posterior à data de início.
        """
        if self.dataInicio and self.dataFim and self.dataFim <= self.dataInicio:
            raise ValidationError({
                'dataFim': 'A data de término deve ser posterior à data de início.'
            })
        # No need to explicitly handle timezones in clean() if using DateTimeField.
        # Django and DRF will do the right thing with timezone-aware objects.