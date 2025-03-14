<template>
  <div class="container py-8 mx-auto">
    <div class="flex items-center mb-6">
      <Button variant="outline" class="mr-4" @click="navigateTo('/')">
        <Icon name="lucide:arrow-left" class="mr-2 h-4 w-4" />
        Voltar
      </Button>
      <h1 class="text-3xl font-bold tracking-tight">Nova Agenda</h1>
    </div>

    <Card>
      <CardContent class="pt-6">
        <form @submit.prevent="submitForm" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Título -->
            <div class="md:col-span-2">
              <Label for="titulo">Título</Label>
              <Input
                id="titulo"
                v-model="form.titulo"
                placeholder="Título da agenda"
                :class="{ 'border-destructive': errors.titulo }"
              />
              <p v-if="errors.titulo" class="text-sm text-destructive mt-1">
                {{ errors.titulo }}
              </p>
            </div>

            <!-- Descrição -->
            <div class="md:col-span-2">
              <Label for="descricao">Descrição</Label>
              <Textarea
                id="descricao"
                v-model="form.descricao"
                placeholder="Descrição detalhada"
                rows="4"
              />
            </div>

            <!-- Data, Hora de Início e Fim (Mesmo Dia) -->
            <div class="md:col-span-2">
              <Label for="data">Data, Hora de Início e Fim</Label>
              <div class="grid grid-cols-3 gap-4 items-end">
                <!-- Data -->
                <Popover>
                  <PopoverTrigger as-child>
                    <Button
                      variant="outline"
                      class="w-full justify-start text-left font-normal"
                      :class="{ 'border-destructive': errors.data }"
                    >
                      <Icon name="lucide:calendar" class="mr-2 h-4 w-4" />
                      <span v-if="!selectedDate">Selecione uma data</span>
                      <span v-else>{{ formatDateDisplay(selectedDate) }}</span>
                    </Button>
                  </PopoverTrigger>
                  <PopoverContent class="w-auto p-0">
                    <Calendar
                      v-model="selectedDate"
                      locale="pt-BR"
                      mode="single"
                      :from-year="2020"
                      :to-year="2030"
                      @update:model-value="handleDateChange"
                    />
                  </PopoverContent>
                </Popover>
                <!-- Hora de Início -->
                <div>
                    <Label for="horaInicio">Hora Início</Label>
                    <Input
                        id="horaInicio"
                        v-model="horaInicio"
                        type="time"
                        :class="{ 'border-destructive': errors.horaInicio }"
                    />
                </div>
                <!-- Hora de Fim -->
                <div>
                   <Label for="horaFim">Hora Fim</Label>
                    <Input
                        id="horaFim"
                        v-model="horaFim"
                        type="time"
                        :class="{ 'border-destructive': errors.horaFim }"
                    />
                </div>

              </div>
              <p v-if="errors.data || errors.horaInicio || errors.horaFim" class="text-sm text-destructive mt-1">
                {{ errors.data || errors.horaInicio || errors.horaFim }}
              </p>
            </div>


            <!-- Local -->
            <div>
              <Label for="local">Local</Label>
              <Input
                id="local"
                v-model="form.local"
                placeholder="Local do evento"
              />
            </div>

            <!-- Status -->
            <div>
              <Label for="estadoAtualAgenda">Status</Label>
              <Select v-model="form.estadoAtualAgenda">
                <SelectTrigger
                  :class="{ 'border-destructive': errors.estadoAtualAgenda }"
                >
                  <SelectValue placeholder="Selecione um status" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="RECEBIDO">Recebido</SelectItem>
                  <SelectItem value="CONFIRMADO">Confirmado</SelectItem>
                  <SelectItem value="CANCELADO">Cancelado</SelectItem>
                  <SelectItem value="ATENDIDO">Atendido</SelectItem>
                </SelectContent>
              </Select>
              <p
                v-if="errors.estadoAtualAgenda"
                class="text-sm text-destructive mt-1"
              >
                {{ errors.estadoAtualAgenda }}
              </p>
            </div>
          </div>

          <!-- Botões -->
          <div class="flex justify-end gap-4">
            <Button type="button" variant="outline" @click="navigateTo('/')">
              Cancelar
            </Button>
            <Button type="submit" :disabled="loading">
              <Icon
                v-if="loading"
                name="lucide:loader-2"
                class="mr-2 h-4 w-4 animate-spin"
              />
              Salvar
            </Button>
          </div>
        </form>
      </CardContent>
    </Card>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import type { AgendaFormData } from '~/types/agenda'
import { Button } from '@/components/ui/button'
import { Card, CardContent } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Textarea } from '@/components/ui/textarea'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from '@/components/ui/popover'
import { Calendar } from '@/components/ui/calendar'
import { useToast } from '@/components/ui/toast/use-toast'
import { format } from 'date-fns';
import { ptBR } from 'date-fns/locale';


const { toast } = useToast()

const loading = ref(false)
const selectedDate = ref<Date | undefined>(undefined)
const horaInicio = ref('08:00')  // Valor padrão
const horaFim = ref('09:00')     // Valor padrão
const errors = ref<Record<string, string>>({})

const form = ref<AgendaFormData>({
  titulo: '',
  descricao: '',
  dataInicio: '',  // Mantém dataInicio e dataFim, mas serão do mesmo dia
  dataFim: '',
  local: '',
  estadoAtualAgenda: 'RECEBIDO',
})

const formatDateDisplay = (date: Date | undefined) => {
  if (!date) return 'Selecione uma data';
  return format(date, "dd/MM/yyyy", { locale: ptBR });
};

const formatDateTimeForApi = (date: Date | null, time: string): string => {
  if (!date) return '';
  
  try {
    const [hours, minutes] = time.split(':');
    const newDate = new Date(date);
    newDate.setHours(parseInt(hours, 10), parseInt(minutes, 10), 0, 0);
    
    // Formato ISO 8601 estrito que será compatível com parseISO
    return newDate.toISOString();
  } catch (error) {
    console.error('Erro ao formatar data/hora para API:', error);
    return '';
  }
}

const handleDateChange = (newDate: Date | undefined) => {
    selectedDate.value = newDate;
    updateDateTimes();
    if (newDate && errors.value.data) {
        delete errors.value.data;
    }
};

// Atualiza dataInicio e dataFim sempre que a data ou as horas mudarem
const updateDateTimes = () => {
  if (selectedDate.value) {
    form.value.dataInicio = formatDateTimeForApi(selectedDate.value, horaInicio.value);
    form.value.dataFim = formatDateTimeForApi(selectedDate.value, horaFim.value);
  }
};

watch(horaInicio, updateDateTimes);
watch(horaFim, updateDateTimes);


const validateForm = (): boolean => {
  const newErrors: Record<string, string> = {}

  if (!form.value.titulo.trim()) {
    newErrors.titulo = 'O título é obrigatório'
  }
  if (!selectedDate.value) {
    newErrors.data = 'A data é obrigatória'
  }
  if (!horaInicio.value) {
    newErrors.horaInicio = 'A hora de início é obrigatória'
  }
  if (!horaFim.value) {
    newErrors.horaFim = 'A hora de fim é obrigatória'
  }
    if (horaInicio.value && horaFim.value) {
    const [startHours, startMinutes] = horaInicio.value.split(':').map(Number);
    const [endHours, endMinutes] = horaFim.value.split(':').map(Number);

    if (startHours > endHours || (startHours === endHours && startMinutes >= endMinutes)) {
      newErrors.horaFim = 'A hora de fim deve ser posterior à hora de início';
    }
  }
  if (!form.value.estadoAtualAgenda) {
    newErrors.estadoAtualAgenda = 'O status é obrigatório'
  }

  errors.value = newErrors;
  return Object.keys(newErrors).length === 0;
}

const submitForm = async () => {
  if (!validateForm()) {
    toast({
      title: 'Formulário inválido',
      description: 'Por favor, corrija os erros no formulário.',
      variant: 'destructive',
    })
    return
  }

  loading.value = true;

  try {
      updateDateTimes(); // Garante que dataInicio e dataFim estão atualizados

    const response = await fetch('http://localhost:8000/api/agendas/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(form.value),
    })

    if (!response.ok) {
       const errorData = await response.json()
        let errorMessage = 'Falha ao criar agenda';
      if (errorData.detail) {
        errorMessage = errorData.detail;
      } else if (typeof errorData === 'object') {
          // Tenta encontrar a primeira mensagem de erro não vazia
        for (const key in errorData) {
          if (Array.isArray(errorData[key]) && errorData[key].length > 0) {
            errorMessage = errorData[key][0];
            break;
          }
        }
      }
      throw new Error(errorMessage);
    }

    toast({
      title: 'Agenda criada',
      description: 'A agenda foi criada com sucesso',
    })

    navigateTo('/')
  } catch (error) {
     console.error('Erro ao criar agenda:', error)
    toast({
      title: 'Erro',
      description:
        error instanceof Error ? error.message : 'Não foi possível criar a agenda',
      variant: 'destructive',
    })
  } finally {
    loading.value = false
  }
}

</script>