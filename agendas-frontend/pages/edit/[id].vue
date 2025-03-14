<template>
  <div class="container py-8 mx-auto">
    <div class="flex items-center mb-6">
      <Button variant="outline" class="mr-4" @click="navigateTo('/')">
        <Icon name="lucide:arrow-left" class="mr-2 h-4 w-4" />
        Voltar
      </Button>
      <h1 class="text-3xl font-bold tracking-tight">Editar Agenda</h1>
    </div>

    <!-- Loading state -->
    <div v-if="fetchLoading" class="flex justify-center items-center p-20">
      <div class="flex flex-col items-center gap-2">
        <Icon name="lucide:loader-2" class="h-10 w-10 animate-spin text-primary" />
        <p class="text-sm text-muted-foreground mt-2">Carregando agenda...</p>
      </div>
    </div>

    <!-- Error state -->
    <div v-else-if="error">
      <Alert variant="destructive" class="mb-6">
        <AlertTitle>Erro</AlertTitle>
        <AlertDescription>{{ error }}</AlertDescription>
      </Alert>
    </div>

    <!-- Form -->
    <Card v-else class="mt-4">
      <CardContent class="pt-6">
        <form @submit.prevent="submitForm" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Título -->
            <div class="md:col-span-2">
              <Label for="title">Título</Label>
              <Input
                id="title"
                v-model="form.title"
                placeholder="Título da agenda"
                :class="{'border-destructive': errors.title}"
              />
              <p v-if="errors.title" class="text-sm text-destructive mt-1">{{ errors.title }}</p>
            </div>

            <!-- Descrição -->
            <div class="md:col-span-2">
              <Label for="description">Descrição</Label>
              <Textarea
                id="description"
                v-model="form.description"
                placeholder="Descrição detalhada"
                rows="4"
              />
            </div>

            <!-- Data - Using a simple date input to avoid Calendar component issues -->
            <div>
              <Label for="date">Data</Label>
              <Input
                id="date"
                v-model="form.date"
                type="date"
                :class="{'border-destructive': errors.date}"
              />
              <p v-if="errors.date" class="text-sm text-destructive mt-1">{{ errors.date }}</p>
            </div>

            <!-- Local -->
            <div>
              <Label for="location">Local</Label>
              <Input
                id="location"
                v-model="form.location"
                placeholder="Local do evento"
              />
            </div>

            <!-- Horário de início -->
            <div>
              <Label for="start_time">Horário de início</Label>
              <Input
                id="start_time"
                v-model="form.start_time"
                type="time"
                :class="{'border-destructive': errors.start_time}"
              />
              <p v-if="errors.start_time" class="text-sm text-destructive mt-1">{{ errors.start_time }}</p>
            </div>

            <!-- Horário de término -->
            <div>
              <Label for="end_time">Horário de término</Label>
              <Input
                id="end_time"
                v-model="form.end_time"
                type="time"
                :class="{'border-destructive': errors.end_time}"
              />
              <p v-if="errors.end_time" class="text-sm text-destructive mt-1">{{ errors.end_time }}</p>
            </div>

            <!-- Status -->
            <div>
              <Label for="status">Status</Label>
              <Select v-model="form.status">
                <SelectTrigger :class="{'border-destructive': errors.status}">
                  <SelectValue placeholder="Selecione um status" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="RECEBIDO">Recebido</SelectItem>
                  <SelectItem value="CONFIRMADO">Confirmado</SelectItem>
                  <SelectItem value="CANCELADO">Cancelado</SelectItem>
                  <SelectItem value="ATENDIDO">Atendido</SelectItem>
                </SelectContent>
              </Select>
              <p v-if="errors.status" class="text-sm text-destructive mt-1">{{ errors.status }}</p>
            </div>
          </div>

          <!-- Botões -->
          <div class="flex justify-end gap-4">
            <Button type="button" variant="outline" @click="navigateTo('/')">
              Cancelar
            </Button>
            <Button type="submit" :disabled="saveLoading">
              <Icon v-if="saveLoading" name="lucide:loader-2" class="mr-2 h-4 animate-spin" />
              Atualizar
            </Button>
          </div>
        </form>
      </CardContent>
    </Card>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import type { AgendaFormData, AgendaApiSubmitData } from '~/types/agenda'
import { Button } from '@/components/ui/button'
import { Card, CardContent } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Textarea } from '@/components/ui/textarea'
import {
  Select, SelectContent, SelectItem,
  SelectTrigger, SelectValue
} from '@/components/ui/select'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'
import { useToast } from '@/components/ui/toast/use-toast'
import { useAgendaApi } from '~/composables/useApi'
import { useRouter, useRoute } from 'vue-router'
import { format, parse } from 'date-fns'

const router = useRouter()
const route = useRoute()
const agendaId = computed(() => Number(route.params.id))
const { toast } = useToast()
const { getAgenda, updateAgenda } = useAgendaApi()

const fetchLoading = ref(true)
const saveLoading = ref(false)
const error = ref<string | null>(null)
const errors = ref<Record<string, string>>({})

const form = ref<AgendaFormData>({
  title: '',
  description: '',
  date: '',
  start_time: '',
  end_time: '',
  location: '',
  status: 'RECEBIDO'
})

onMounted(async () => {
  await fetchAgenda()
})

const fetchAgenda = async () => {
  fetchLoading.value = true
  error.value = null

  try {
    const response = await getAgenda(agendaId.value)
    const agendaData = response.data || response

    if (agendaData && agendaData.titulo) {
      // Set basic form data
      form.value = {
        title: agendaData.titulo || '',
        description: agendaData.descricao || '',
        location: agendaData.local || '',
        status: agendaData.estadoAtualAgenda || 'RECEBIDO',
        date: '',
        start_time: '',
        end_time: ''
      }

      // Process start date
      if (agendaData.dataInicio) {
        try {
          const startDate = new Date(agendaData.dataInicio)
          if (!isNaN(startDate.getTime())) {
            // Format date for input[type=date] - YYYY-MM-DD
            form.value.date = format(startDate, 'yyyy-MM-dd')
            form.value.start_time = format(startDate, 'HH:mm')
          }
        } catch (err) {
          console.error('Erro ao processar data de início:', err)
        }
      }

      // Process end date
      if (agendaData.dataFim) {
        try {
          const endDate = new Date(agendaData.dataFim)
          if (!isNaN(endDate.getTime())) {
            form.value.end_time = format(endDate, 'HH:mm')
          }
        } catch (err) {
          console.error('Erro ao processar data de término:', err)
        }
      }
    } else if (response.error) {
      error.value = response.error
    } else {
      error.value = 'Dados da agenda não encontrados'
    }
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Erro ao buscar agenda'
  } finally {
    fetchLoading.value = false
  }
}

const validateForm = (): boolean => {
  const newErrors: Record<string, string> = {}

  if (!form.value.title.trim()) {
    newErrors.title = 'O título é obrigatório'
  }
  if (!form.value.date) {
    newErrors.date = 'A data é obrigatória'
  }
  if (!form.value.start_time) {
    newErrors.start_time = 'O horário de início é obrigatório'
  }
  if (!form.value.end_time) {
    newErrors.end_time = 'O horário de término é obrigatório'
  }
  if (!form.value.status) {
    newErrors.status = 'O status é obrigatório'
  }

  errors.value = newErrors
  return Object.keys(newErrors).length === 0
}

const submitForm = async () => {
  if (!validateForm()) {
    toast({
      title: 'Formulário inválido',
      description: 'Por favor, preencha todos os campos obrigatórios',
      variant: 'destructive'
    })
    return
  }

  saveLoading.value = true

  try {
    let dataInicio = null
    let dataFim = null

    if (form.value.date && form.value.start_time) {
      dataInicio = `${form.value.date}T${form.value.start_time}:00.000Z`
    }
    if (form.value.date && form.value.end_time) {
      dataFim = `${form.value.date}T${form.value.end_time}:00.000Z`
    }

    const agendaData: AgendaApiSubmitData = {
      titulo: form.value.title,
      descricao: form.value.description,
      dataInicio: dataInicio,
      dataFim: dataFim,
      local: form.value.location,
      estadoAtualAgenda: form.value.status as 'RECEBIDO' | 'CONFIRMADO' | 'CANCELADO' | 'ATENDIDO'
    }

    const response = await updateAgenda(agendaId.value, agendaData)

    if (response.data) {
      toast({
        title: 'Agenda atualizada',
        description: 'A agenda foi atualizada com sucesso'
      })
      navigateTo('/')
    } else if (response.error) {
      throw new Error(response.error)
    }
  } catch (error: any) {
    toast({
      title: 'Erro',
      description: error.message || 'Não foi possível atualizar a agenda',
      variant: 'destructive'
    })
  } finally {
    saveLoading.value = false
  }
}

const navigateTo = (path: string) => {
  router.push(path)
}
</script>