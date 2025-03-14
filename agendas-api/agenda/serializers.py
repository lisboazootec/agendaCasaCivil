from rest_framework import serializers
from .models import Agenda

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['id', 'titulo', 'descricao', 'dataInicio', 'dataFim',
                  'local', 'estadoAtualAgenda', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        """
        Verifica se a data final é posterior à data inicial.
        """
        if 'dataInicio' in data and 'dataFim' in data:
            if data['dataFim'] <= data['dataInicio']:
                raise serializers.ValidationError({
                    "dataFim": "A data de término deve ser posterior à data de início."
                })
        return data